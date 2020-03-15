from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from uuid import uuid1

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

    def get_second_name(self):
        return self.second_name

    def get_surname(self):
        return self.surname

    def get_all_info(self):
        return {self.id: [self.name, self.second_name, self.surname]}


# staff_list = [
#     Person(11111111, 'name1', 'second_name1', 'surname1'),
#     Person(11111112, 'name2', 'second_name2', 'surname2'),
#     Person(11111113, 'name3', 'second_name3', 'surname3'),
#     Person(11111114, 'name4', 'second_name4', 'surname4'),
#     Person(11111115, 'name5', 'second_name5', 'surname5'),
#
# ]
staff_list = [(Person(uuid1().__str__(), "name" + str(i), 'second_name' + str(i), "surname" + str(i))) for i in
              range(5)]


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


@app.route('/staff', methods=['GET', 'POST'])
def staff_methods():
    if request.method == 'GET':
        all_info = [i.get_all_info() for i in staff_list]
        return jsonify(all_info)
    elif request.method == 'POST':
        name = 'name6'
        second_name = 'second_name6'
        surname = "surname6"
        per_id = uuid1().__str__()
        if in_person_search(surname, staff_list):
            staff_list.append(Person(per_id, name, second_name, surname))
            all_info = [i.get_all_info() for i in staff_list]
            return jsonify(all_info)
        else:
            replay = "This person already in list"
            return jsonify(replay)
    else:
        return status.HTTP_404_NOT_FOUND


@app.route('/staff/<person_id>', methods=['GET', 'PUT', 'DELETE'])
def member_page(person_id):
    if request.method == 'GET':
        try:
            person = in_person_search_by_id(person_id, staff_list)
            return jsonify(person.get_all_info())
        except:
            return jsonify(status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            person_index = search_for_index(person_id, staff_list)
            staff_list[person_index] = Person('14bb99d4-66ba-11ea-b96a-f07960024c26', 'Alec', 'second_name0',
                                              'Andriiets')
            return jsonify(status.HTTP_200_OK)
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
