from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from uuid import uuid1
from json import loads
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

posge_host = os.environ.get("POSGRESQL-HOSTNAME") or 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nprl:nprl@' + posge_host + ':5432/nprl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
cors = CORS(app)

from classes.person_class import *
from classes.project_class import *
from classes.tracker_class import *


@app.route('/staff', methods=['GET', 'POST'])
def staff_page_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in Staff.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        person = Staff(uuid1().__str__(), request_info['name'], request_info['second_name'], request_info['surname'])
        db.session.add(person)
        db.session.commit()
        return jsonify(person.serialize)
    else:
        return status.HTTP_404_NOT_FOUND


@app.route('/staff/<person_id>', methods=['GET', 'PUT', 'DELETE'])
def member_page_methods(person_id):
    if request.method == 'GET':
        try:
            person = Staff.query.get(person_id)
            return jsonify(person.serialize)
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            request_info = loads(request.data.decode('utf-8'))
            person = Staff.query.get(person_id)
            person.name = request_info['name']
            person.second_name = request_info['second_name']
            person.surname = request_info['surname']
            db.session.commit()
            return jsonify(status.HTTP_200_OK, person.serialize)
        except NameError:
            return jsonify(status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            person = Staff.query.get(person_id)
            db.session.delete(person)
            db.session.commit()
            return jsonify(status.HTTP_200_OK)
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)


@app.route('/projects', methods=['GET', 'POST'])
def projects_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in Project.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        project = Project(uuid1().__str__(), request_info['name'], request_info['rate'])
        db.session.add(project)
        db.session.commit()
        return jsonify([i.serialize for i in Project.query.all()])
    else:
        return jsonify(status.HTTP_404_NOT_FOUND)


@app.route('/projects/<project_id>', methods=['GET', 'PUT', 'DELETE'])
def project_paje(project_id):
    if request.method == 'GET':
        try:
            project = Project.query.get(project_id)
            return jsonify(project.serialize)
        except:
            jsonify(status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            request_info = loads(request.data.decode('utf-8'))
            person = Project.query.get(project_id)
            person.name = request_info['name']
            person.rate = request_info['rate']
            db.session.commit()
            return jsonify(status.HTTP_200_OK, person.serialize)
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            project = Project.query.get(project_id)
            db.session.delete(project)
            db.session.commit()
            return jsonify(status.HTTP_200_OK)
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)


@app.route('/time', methods=['GET', 'POST', 'DELETE'])
def trekker_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in Time.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        project = Time(uuid1().__str__(), request_info['per_id'], request_info['pro_id'], request_info['time'])
        db.session.add(project)
        db.session.commit()
        return jsonify([i.serialize for i in Time.query.all()])
    else:
        return jsonify(status.HTTP_404_NOT_FOUND)


@app.route('/time/<time_id>', methods=['PUT', 'DELETE'])
def time_method(time_id):
    if request.method == 'PUT':
        return jsonify(Time.query.get(time_id))
    elif request.method == 'DELETE':
        try:
            person = Staff.query.get(time_id)
            db.session.delete(person)
            db.session.commit()
            return jsonify(status.HTTP_200_OK)
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)


if __name__ == "__main__":
    app.run()
