FROM python:3.9.7

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["python", "-u", "app/app.py"]

# update_container.sh v1.2.6
# docker rmi udaconnect-notifications-service
# docker build -t udaconnect-notifications-service .

# docker tag udaconnect-notifications-service hosamelbasiony/udaconnect-notifications-service:v1.2.5
# docker push hosamelbasiony/udaconnect-notifications-service:v1.2.5