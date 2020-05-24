from flask import Flask, Response
from flask import jsonify
from flask import request
from uuid import uuid1
from json import loads
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

postgre_host = os.environ.get("POSGRESQL-HOSTNAME") or 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://univ_pr:univ_pr@' + postgre_host + ':5432/univ_pr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
cors = CORS(app)

from classes.person_class import *
from classes.project_class import *
from classes.tracker_class import *
from classes.position_class import *
from classes.work_type_class import *
from classes.public_salary_table import *


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


def for_staff_check(per_id):
    list_with_time_elems = [i.serialize for i in TimeTracker.query.all()]
    for i in list_with_time_elems:
        if i["staffId"] == per_id:
            return True


def for_projects_check(pro_id):
    list_with_time_elems = [i.serialize for i in TimeTracker.query.all()]
    for i in list_with_time_elems:
        if i["projectId"] == pro_id:
            return True


def for_positions_check(pos_id):
    list_with_staff_elems = [i.serialize for i in Staff.query.all()]
    for i in list_with_staff_elems:
        if i["positionId"] == pos_id:
            return True


def for_work_type_check(wt_id):
    list_with_time_elems = [i.serialize for i in TimeTracker.query.all()]
    for i in list_with_time_elems:
        if i["workTypeId"] == wt_id:
            return True


def remove_false(arg):
    return {k: v for k, v in arg.items() if v is not None and v != ''}


@app.route('/staff', methods=['GET', 'POST'])
def staff_page_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in Staff.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        uuid = uuid1().__str__()
        person = Staff(uuid, request_info['name'], request_info['surname'], request_info['position'])
        db.session.add(person)
        db.session.commit()
        return jsonify(person.serialize)
    else:
        return jsonify({'message': 'Error'}), 404


@app.route('/staff/<person_id>', methods=['GET', 'PUT', 'DELETE'])
def member_page_methods(person_id):
    if request.method == 'GET':
        try:
            person = Staff.query.get(person_id)
            return jsonify(person.serialize)
        except:
            return jsonify({'message': 'Not found'}), 400
    elif request.method == 'PUT':
        try:
            request_info = loads(request.data.decode('utf-8'))
            person = Staff.query.get(person_id)
            person.name = request_info['name']
            person.surname = request_info['surname']
            person.position_id = request_info['positionId']
            person.updated_at = datetime.datetime.utcnow()
            db.session.commit()
            return jsonify(person.serialize)
        except NameError:
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'DELETE':
        try:
            if for_staff_check(person_id):
                return jsonify({'message': 'Element can`t be deleted'}), 400
            person = Staff.query.get(person_id)
            db.session.delete(person)
            db.session.commit()
            return jsonify({'message': 'Successfully deleted '}), 200
        except:
            return jsonify({'message': 'Error'}), 404


@app.route('/projects', methods=['GET', 'POST'])
def projects_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in Project.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        uuid = uuid1().__str__()
        project = Project(uuid, request_info['name'])
        db.session.add(project)
        db.session.commit()
        return jsonify(project.serialize)
    else:
        return jsonify({'message': 'Error'}), 404


@app.route('/projects/<project_id>', methods=['GET', 'PUT', 'DELETE'])
def project_page(project_id):
    if request.method == 'GET':
        try:
            project = Project.query.get(project_id)
            return jsonify(project.serialize)
        except:
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'PUT':
        try:
            request_info = loads(request.data.decode('utf-8'))
            person = Project.query.get(project_id)
            person.name = request_info['name']
            db.session.commit()
            return jsonify(person.serialize)
        except:
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'DELETE':
        try:
            if for_staff_check(project_id):
                return jsonify({'message': 'Element can`t be deleted'}), 400
            project = Project.query.get(project_id)
            db.session.delete(project)
            db.session.commit()
            return jsonify({'message': 'Successfully deleted '}), 200
        except:
            return jsonify({'message': 'Error'}), 404


@app.route('/time-tracker', methods=['GET', 'POST'])
def trekker_methods():
    if request.method == 'GET':
        if request.query_string:
            filer_params = {}
            date1 = None
            date2 = None

            if 'project' in request.args.keys():
                filer_params['project_id'] = request.args.get('project')

            if 'user' in request.args.keys():
                filer_params['staff_id'] = request.args.get('user')

            if 'date1' in request.args.keys():
                if request.args.get('date1') != '':
                    date1 = request.args.get('date1') + ' 00:00:00'
                    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')

            if 'date2' in request.args.keys():
                if request.args.get('date2') != '':
                    date2 = request.args.get('date2') + ' 23:59:59'
                    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

            if date1 and date2:
                filer_params = remove_false(filer_params)
                filtered_by = TimeTracker.query.filter_by(**filer_params).filter(
                    TimeTracker.create_at.between(date1, date2))
            else:
                filer_params = remove_false(filer_params)
                filtered_by = TimeTracker.query.filter_by(**filer_params)
            return jsonify([i.serialize for i in filtered_by])
        else:
            work_records = TimeTracker.query.all()
            db.session.commit()
            serialized_rows = [i.serialize for i in work_records]
            return jsonify(serialized_rows)
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        uuid = uuid1().__str__()
        time_track = TimeTracker(uuid, request_info['perId'], request_info['proId'], request_info['workTypeId'],
                                 request_info['time'])
        db.session.add(time_track)
        db.session.commit()
        return jsonify(time_track.serialize)
    else:
        return jsonify({'message': 'Error'}), 404


@app.route('/time-tracker/<time_id>', methods=['GET', 'DELETE'])
def time_method(time_id):
    if request.method == 'GET':
        return jsonify(TimeTracker.query.get(time_id))
    elif request.method == 'DELETE':
        try:
            time_elem = TimeTracker.query.get(time_id)
            db.session.delete(time_elem)
            db.session.commit()
            return jsonify({'message': 'Successfully deleted '}), 200
        except:
            return jsonify({'message': 'Error'}), 404


@app.route('/positions', methods=['GET', 'POST'])
def positions_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in Position.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        uuid = uuid1().__str__()
        position = Position(uuid, request_info['name'], request_info['salary'])
        db.session.add(position)
        db.session.commit()
        return jsonify(position.serialize)
    else:
        return jsonify({'message': 'Error'}), 404


@app.route('/positions/<position_id>', methods=['GET', 'PUT', 'DELETE'])
def position_page(position_id):
    if request.method == 'GET':
        try:
            position = Position.query.get(position_id)
            return jsonify(position.serialize)
        except:
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'PUT':
        try:
            request_info = loads(request.data.decode('utf-8'))
            position = Position.query.get(position_id)
            position.name = request_info['name']
            position.salary = request_info['salary']
            db.session.commit()
            return jsonify(position.serialize)
        except:
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'DELETE':
        try:
            if for_positions_check(position_id):
                return jsonify({'message': 'Element can`t be deleted'}), 400
            position = Position.query.get(position_id)
            db.session.delete(position)
            db.session.commit()
            return jsonify({'message': 'Successfully deleted '}), 200
        except NameError:
            print(NameError)
            return jsonify({'message': 'Error'}), 404


@app.route('/work-type', methods=['GET', 'POST'])
def work_type_methods():
    if request.method == 'GET':
        return jsonify([i.serialize for i in WorkType.query.all()])
    elif request.method == 'POST':
        request_info = loads(request.data.decode('utf-8'))
        uuid = uuid1().__str__()
        work_type = WorkType(uuid, request_info['name'], request_info['salary'])
        db.session.add(work_type)
        db.session.commit()
        return jsonify(work_type.serialize)
    else:
        return jsonify({'message': 'Error'}), 404


@app.route('/work-type/<work_type_id>', methods=['GET', 'PUT', 'DELETE'])
def work_type_page(work_type_id):
    if request.method == 'GET':
        try:
            work_type = WorkType.query.get(work_type_id)
            return jsonify(work_type.serialize)
        except:
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'PUT':
        try:
            request_info = loads(request.data.decode('utf-8'))
            work_type = WorkType.query.get(work_type_id)
            work_type.name = request_info['name']
            work_type.salary_mod = request_info['salaryMod']
            db.session.commit()
            return jsonify(work_type.serialize)
        except NameError:
            print(NameError)
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'DELETE':
        try:
            if for_work_type_check(work_type_id):
                return jsonify({'message': 'Element can`t be deleted'}), 400
            work_type = WorkType.query.get(work_type_id)
            db.session.delete(work_type)
            db.session.commit()
            return jsonify({'message': 'Successfully deleted '}), 200
        except:
            return jsonify({'message': 'Error'}), 404


@app.route('/month_time_sheet', methods=['GET', "POST"])
def salary_calc():
    if request.method == 'GET':
        try:
            time_sheet = MonthTimeSheet.query.all()
            return jsonify([i.serialize for i in time_sheet])
        except:
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'POST':
        try:
            request_info = loads(request.data.decode('utf-8'))
            uuid = uuid1().__str__()
            time_sheet = MonthTimeSheet(uuid, request_info['personId'], request_info['salary'], request_info['pStart'],
                                        request_info['pEnd'])
            db.session.add(time_sheet)
            db.session.commit()
            return jsonify(time_sheet.serialize)
        except:
            return jsonify({'message': 'Error'}), 404


@app.route('/month_time_sheet/<time_sheet_id>', methods=['GET', 'DELETE'])
def sheet_id(time_sheet_id):
    if request.method == 'GET':
        try:
            sheet = TimeTracker.query.filter_by(head_id=time_sheet_id)
            return [i.serialize for i in sheet]
        except:
            return jsonify({'message': 'Error'}), 404
    elif request.method == 'DELETE':
        try:
            month_sheet = MonthTimeSheet.query.get(time_sheet_id)
            db.session.delete(month_sheet)
            db.session.commit()
            return jsonify({'message': 'Successfully deleted '}), 200
        except:
            return jsonify({'message': 'Error'}), 404


if __name__ == "__main__":
    app.run()
