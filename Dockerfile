FROM python:3.10.1-alpine

WORKDIR /PythonDocker

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
