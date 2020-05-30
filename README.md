# University project
it's a project for my university.

### Requirements

1. Docker from [a link](https://www.docker.com/)

2. Python3.7 from [a link](https://www.python.org/downloads/)


## Local Development

Firstly we run data base PosgreSQL in docker compose

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

Run docker compose with command below

```
$ docker-compose -f docker-compose.yaml up
```

and then go to given link or [a link](http://0.0.0.0:5000/)