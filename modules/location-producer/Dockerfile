FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5001

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]


# docker rmi udaconnect-location-producer
# docker build -t udaconnect-location-producer .

# docker run -d -p 5555:5000 udaconnect-location-producer:v1.1.4

# docker tag udaconnect-location-producer hosamelbasiony/udaconnect-location-producer:v1.1.4
# docker push hosamelbasiony/udaconnect-location-producer:v1.1.4


# flask run --host 0.0.0.0 --port 5001