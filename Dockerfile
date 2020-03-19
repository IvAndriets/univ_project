FROM python:3.7

RUN pip install pipenv

WORKDIR /falsk_test

COPY Pipfile .
COPY Pipfile.lock .
COPY classes ./classes

RUN pipenv install --system --deploy --ignore-pipfile

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt


COPY app.py .

RUN echo Hello world
RUN chmod +x ./app.py

EXPOSE 8080:8080

CMD ["python", "./app.py"]
