from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from uuid import uuid1
import ast

app = Flask(__name__)


class Person:
    def __init__(self, person_id, name, second_name, surname):
        self.id = person_id
        self.name = name
        self.second_name = second_name
        self.surname = surname

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def change_name(self, name):
        self.name = name

    def get_second_name(self):
        return self.second_name

    def change_second_name(self, second_name):
        self.second_name = second_name

    def get_surname(self):
        return self.surname

    def change_surname(self, surname):
        self.surname = surname

    def change_all_info(self, name, second_name, surname):
        self.name = name
        self.second_name = second_name
        self.surname = surname

    def get_all_info(self):
        return {'person_id': self.id, 'name': self.name, 'surname': self.surname, 'second_name': self.second_name}



staff_list = [Person("99d3de6c-66f4-11ea-8ec1-f07960024c26", "name0", 'second_name0', "surname0"),
              Person("99d3e164-66f4-11ea-8ec1-f07960024c26", "name1", 'second_name1', "surname1"),
              Person("99d3e1e6-66f4-11ea-8ec1-f07960024c26", "name2", 'second_name2', "surname2"),
              Person("99d3e1e6-66f4-11ea-8ec1-f07960024c26", "name3", 'second_name3', "surname3"),
              Person("99d3e2a4-66f4-11ea-8ec1-f07960024c26", "name4", 'second_name4', "surname4")]


def in_person_search(surname, list_to_search):
    for i in list_to_search:
        if i.get_surname() == surname:
            return False
    return Exception


def in_person_search_by_id(person_id, list_to_search):
    for i in list_to_search:
        if i.get_id() == person_id:
            return i
    return Exception


def search_for_index(person_id, list_to_search):
    for i in range(len(list_to_search)):
        if list_to_search[i].get_id() == person_id:
            return i
    return Exception


def validator(dict_with_persons_info):
    if 'person_id' in dict_with_persons_info.keys():
        return Exception
    elif dict_with_persons_info["name"] is None:
        return Exception
    elif dict_with_persons_info["second_name"] is None:
        return Exception
    elif dict_with_persons_info["surname"] is None:
        return Exception


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
