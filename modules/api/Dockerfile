FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

# docker rmi udaconnect-api
# docker build -t udaconnect-api .

# docker tag udaconnect-api hosamelbasiony/udaconnect-api:v1.0.8
# docker push hosamelbasiony/udaconnect-api:v1.0.8