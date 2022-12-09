FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5003

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5003"]

# sudo ./update_container.sh v1.0.6

# flask run --host 0.0.0.0 --port 5003