# University project
It's a project for my university.

### Requirements

1. Docker v19.03 from [a link](https://www.docker.com/)

2. Python3.7.7 from [a link](https://www.python.org/downloads/release/python-377/)

## Local Development

Firstly we run data base PostgreSQL in docker compose

```
$ docker-compose -f docker-compose.lock.yaml up
```

Then install virtual environment Pipenv

```
$ pip install pipenv
```

then activate your virtual environment

```
$ pipenv shell
```

install all requirements

```
$ pip install -r Pipfile.lock
```

and run project

```
$ pipenv run python app.py
```


## Run in production

Setup Flask and Apache to [wsgi](https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/) mod 

Run docker compose with command below

```
$ docker-compose -f docker-compose.yaml up
```

and then go to given link or [a link](http://0.0.0.0:5000/)
