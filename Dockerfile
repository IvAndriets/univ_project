FROM python:3.7

RUN pip install pipenv

WORKDIR /univ_project

COPY Pipfile .
COPY Pipfile.lock .
COPY classes ./classes
COPY app.py .

RUN pipenv install --system --deploy --ignore-pipfile

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD ["flask", "run"]