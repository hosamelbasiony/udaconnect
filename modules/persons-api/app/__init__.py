from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect API", version="0.1.0")

    #################################################################
    ################################################################
    ## TRACING #####################################################
    ################################################################    
    import logging  
    from jaeger_client import Config
    from flask_opentracing import FlaskTracing  
    config = Config(
    config={
            'sampler':
            {'type': 'const',
            'param': 1},
                            'logging': True,
                            'reporter_batch_size': 1,}, 
                            service_name="udaconnect-service")
    jaeger_tracer = config.initialize_tracer()
    tracing = FlaskTracing(jaeger_tracer, True, app)
    with jaeger_tracer.start_span("persons-api-span") as span:
        span.set_tag("persons-api-tag", "100")
    ################################################################
    ################################################################

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
