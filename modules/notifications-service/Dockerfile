FROM python:3.9.7

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["python", "-u", "app/app.py"]

# ./update_container.sh v1.4.2