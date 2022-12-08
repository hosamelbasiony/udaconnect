FROM python:3.9.7

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5002

COPY . .
CMD ["python", "-u", "app/udaconnect/consumer.py"]

# sudo ./update_container.sh v1.1.6

# docker rmi udaconnect-location-consumer
# docker build -t udaconnect-location-consumer .
# docker run -d -p 5555:5000 udaconnect-location-consumer:v1.0.7
# docker tag udaconnect-location-consumer hosamelbasiony/udaconnect-location-consumer:v1.0.7
# docker push hosamelbasiony/udaconnect-location-consumer:v1.0.7