from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from classes.project_class import *

app = Flask(__name__)


project_list = [
    Project('cfa453c4-6838-11ea-b6ff-f07960024c26', 'P_name_1', 1),
    Project('cfa45702-6838-11ea-b6ff-f07960024c26', 'P_name_2', 2),
    Project('cfa457a2-6838-11ea-b6ff-f07960024c26', 'P_name_3', 3),
    Project('cfa45838-6838-11ea-b6ff-f07960024c26', 'P_name_4', 4),
    Project('cfa458a6-6838-11ea-b6ff-f07960024c26', 'P_name_5', 5),
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