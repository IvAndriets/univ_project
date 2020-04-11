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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://univ_pr:univ_pr@' + posge_host + ':5432/univ_pr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
cors = CORS(app)

from classes.person_class import *
from classes.project_class import *
from classes.tracker_class import *


def for_staff_check(per_id):
    list_with_time_elems = [i.serialize for i in Time.query.all()]
    for i in list_with_time_elems:
        if i["staff_id"] == per_id:
            return True


def for_projects_check(pro_id):
    list_with_time_elems = [i.serialize for i in Time.query.all()]
    for i in list_with_time_elems:
        if i["project_id"] == pro_id:
            return True


# @app.route('/main',  methods=['GET'])
# def main():
#     staff = [i.serialize for i in Staff.query.all()]
#     projects = [i.serialize for i in Project.query.all()]
#     time_tracker = [i.serialize for i in Time.query.all()]


@app.route('/staff', methods=['GET', 'POST'])
def staff_page_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in Staff.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        uuid = uuid1().__str__()
        person = Staff(uuid, request_info['name'], request_info['second_name'], request_info['surname'])
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
            if for_staff_check(person_id):
                return status.HTTP_400_BAD_REQUEST
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
        uuid = uuid1().__str__()
        project = Project(uuid, request_info['name'], request_info['rate'])
        db.session.add(project)
        db.session.commit()
        return jsonify(project.serialize)
    else:
        return jsonify(status.HTTP_404_NOT_FOUND)


@app.route('/projects/<project_id>', methods=['GET', 'PUT', 'DELETE'])
def project_page(project_id):
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
            if for_staff_check(project_id):
                return status.HTTP_400_BAD_REQUEST
            project = Project.query.get(project_id)
            db.session.delete(project)
            db.session.commit()
            return jsonify(status.HTTP_200_OK)
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)


@app.route('/time-tracker', methods=['GET', 'POST'])
def trekker_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in Time.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        uuid = uuid1().__str__()
        time_track = Time(uuid, request_info['per_id'], request_info['pro_id'], request_info['time'])
        db.session.add(time_track)
        db.session.commit()
        return jsonify(time_track.serialize)
    else:
        return jsonify(status.HTTP_404_NOT_FOUND)


@app.route('/time-tracker/<time_id>', methods=['GET', 'DELETE'])
def time_method(time_id):
    if request.method == 'GET':
        return jsonify(Time.query.get(time_id))
    elif request.method == 'DELETE':
        try:
            time_elem = Time.query.get(time_id)
            db.session.delete(time_elem)
            db.session.commit()
            return jsonify(status.HTTP_200_OK)
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)


if __name__ == "__main__":
    app.run()
