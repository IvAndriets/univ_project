from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from uuid import uuid1

app = Flask(__name__)


class Project:
    def __init__(self, project_id, project_name, project_rate):
        self.project_id = project_id
        self.project_name = project_name
        self.project_rate = project_rate

    def get_id(self):
        return jsonify(self.project_id)

    def get_name(self):
        return jsonify(self.project_name)

    def gat_project_rate(self):
        return jsonify(self.project_rate)

    def get_all_info(self):
        return {self.project_id: [self.project_name, self.project_rate]}


project_list = [
    Project(10000001, 'P_name_1', 1),
    Project(10000002, 'P_name_2', 2),
    Project(10000003, 'P_name_3', 3),
    Project(10000004, 'P_name_4', 4),
    Project(10000005, 'P_name_5', 5),
]


@app.route('/projects', methods=['GET', 'POST', 'PUT', 'DELETE'])
def projects_methods():
    if request.method == 'GET':
        x = [i.get_all_info() for i in project_list]
        return jsonify(x)
    elif request.method == 'POST':
        x = [i.get_all_info() for i in project_list]
        return jsonify(x)
    elif request.method == 'PUT':
        y = [i.get_all_info() for i in project_list]
        x = Project(10000006, 'P_name_6', 6)
        if x.get_all_info() not in y:
            project_list.append(x)
        else:
            print('Already included')
        y = [i.get_all_info() for i in project_list]
        return jsonify(y)
    elif request.method == 'DELETE':
        y = [i.get_all_info() for i in project_list]
        x = Project(10000006, 'P_name_6', 6)
        if x.get_all_info() in y:
            project_list.pop()
        else:
            print('Already not included')
        y = [i.get_all_info() for i in project_list]
        return jsonify(y)
    else:
        print('Error')
        return


if __name__ == '__main__':
    app.run(debug=True)