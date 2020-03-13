from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


class Person:
    def __init__(self, per_id, name, second_name, surname):
        self.id = per_id
        self.name = name
        self.second_name = second_name
        self.surname = surname

    def get_info(self):
        return {self.id: [self.name, self.second_name, self.surname]}


class Project:
    def __init__(self, pr_id, pr_name, pr_rate):
        self.pr_id = pr_id
        self.pr_name = pr_name
        self.pr_rate = pr_rate

    def get_ifo(self):
        return {self.pr_id: [self.pr_name, self.pr_rate]}


class Time:
    def __init__(self, per_id, pro_id, time):
        self.per_id = per_id
        self.pro_id = pro_id
        self.time = time

    def get_info(self):
        return {[self.per_id, self.pro_id]: self.time}


staff_list = [
    Person(11111111, 'name1', 'second_name1', 'surname1'),
    Person(11111112, 'name2', 'second_name2', 'surname2'),
    Person(11111113, 'name3', 'second_name3', 'surname3'),
    Person(11111114, 'name4', 'second_name4', 'surname4'),
    Person(11111115, 'name5', 'second_name5', 'surname5'),

]
project_list = [
    Project(10000001, 'P_name_1', 1),
    Project(10000002, 'P_name_2', 2),
    Project(10000003, 'P_name_3', 3),
    Project(10000004, 'P_name_4', 4),
    Project(10000005, 'P_name_5', 5),
]
trekker_list = [
    Time(10000001, 11111111, 10),
    Time(10000001, 11111111, 10),
    Time(10000001, 11111111, 10),
    Time(10000001, 11111111, 10),
    Time(10000001, 11111111, 10),
]


@app.route('/staff', methods=['GET', 'POST', 'PUT', 'DELETE'])
def staff_methods():
    if request.method == 'GET':
        x = [i.get_info() for i in staff_list]
        return jsonify(x)
    elif request.method == 'POST':
        x = [i.get_info() for i in staff_list]
        return jsonify(x)
    elif request.method == 'PUT':
        y = [i.get_info() for i in staff_list]
        x = Person(11111116, 'name6', 'second_name6', 'surname6')
        if x.get_info() not in y:
            staff_list.append(x)
        else:
            print('Already included')
        y = [i.get_info() for i in staff_list]
        return jsonify(y)
    elif request.method == 'DELETE':
        y = [i.get_info() for i in staff_list]
        x = Person(11111116, 'name6', 'second_name6', 'surname6')
        if x.get_info() in y:
            staff_list.pop()
        else:
            print('Already not included')
        y = [i.get_info() for i in staff_list]
        return jsonify(y)
    else:
        print('Error')
        return


@app.route('/projects', methods=['GET', 'POST', 'PUT', 'DELETE'])
def projects_methods():
    if request.method == 'GET':
        x = [i.get_ifo() for i in project_list]
        return jsonify(x)
    elif request.method == 'POST':
        x = [i.get_ifo() for i in project_list]
        return jsonify(x)
    elif request.method == 'PUT':
        y = [i.get_ifo() for i in project_list]
        x = Project(10000006, 'P_name_6', 6)
        if x.get_ifo() not in y:
            project_list.append(x)
        else:
            print('Already included')
        y = [i.get_ifo() for i in project_list]
        return jsonify(y)
    elif request.method == 'DELETE':
        y = [i.get_ifo() for i in project_list]
        x = Project(10000006, 'P_name_6', 6)
        if x.get_ifo() in y:
            project_list.pop()
        else:
            print('Already not included')
        y = [i.get_ifo() for i in project_list]
        return jsonify(y)
    else:
        print('Error')
        return


@app.route('/time', methods=['GET', 'POST', 'PUT', 'DELETE'])
def projects_methods():
    if request.method == 'GET':
        get_ifo_list = [i.get_info() for i in trekker_list]
        return jsonify(get_ifo_list)
    elif request.method == 'POST':
        get_ifo_list = [i.get_info() for i in trekker_list]
        return jsonify(get_ifo_list)
    elif request.method == 'PUT':
        get_ifo_list = [i.get_info() for i in trekker_list]
        return jsonify(get_ifo_list)
    elif request.method == 'DELETE':
        get_ifo_list = [i.get_info() for i in trekker_list]
        return jsonify(get_ifo_list)


if __name__ == '__main__':
    app.run(debug=True)
