FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5001

COPY . .
CMD ["python", "app.py"]
# CMD ["flask", "run", "--host", "0.0.0.0"]