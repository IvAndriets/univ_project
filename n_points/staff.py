from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from uuid import uuid1
import ast
from classes.person_class import *

app = Flask(__name__)


staff_list = [Person("99d3de6c-66f4-11ea-8ec1-f07960024c26", "name0", 'second_name0', "surname0"),
              Person("99d3e164-66f4-11ea-8ec1-f07960024c26", "name1", 'second_name1', "surname1"),
              Person("99d3e1e6-66f4-11ea-8ec1-f07960024c26", "name2", 'second_name2', "surname2"),
              Person("99d3e1e6-66f4-11ea-8ec1-f07960024c26", "name3", 'second_name3', "surname3"),
              Person("99d3e2a4-66f4-11ea-8ec1-f07960024c26", "name4", 'second_name4', "surname4")]


@app.route('/staff', methods=['GET', 'POST'])
def staff_page_methods():
    if request.method == 'GET':
        all_info = [i.get_all_info() for i in staff_list]
        return jsonify(all_info)
    elif request.method == 'POST':
        request_info = ast.literal_eval(request.data.decode('utf-8'))
        per_id = uuid1().__str__()
        if in_person_search(request_info["surname"], staff_list):
            staff_list.append(Person(per_id, request_info['name'], request_info['second_name'], request_info['surname']))
            all_info = [i.get_all_info() for i in staff_list]
            return jsonify(all_info)
        else:
            replay = "This person already in list"
            return jsonify(replay)
    else:
        return status.HTTP_404_NOT_FOUND


@app.route('/staff/<person_id>', methods=['GET', 'PUT', 'DELETE'])
def member_page_methods(person_id):
    if request.method == 'GET':
        try:
            person = in_person_search_by_id(person_id, staff_list)
            return jsonify(person.get_all_info())
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            person = in_person_search_by_id(person_id, staff_list)
            request_info = ast.literal_eval(request.data.decode('utf-8'))

            validator(request_info)
            person.change_all_info(request_info['name'], request_info['second_name'],
                                   request_info['surname'])
            return jsonify(status.HTTP_200_OK, person.get_all_info())
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            person_index = search_for_index(person_id, staff_list)
            del staff_list[person_index]
            return jsonify(status.HTTP_200_OK)
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)


if __name__ == '__main__':
    app.run(debug=True)
