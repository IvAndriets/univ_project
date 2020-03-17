from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from classes.tracker_class import *

app = Flask(__name__)

trekker_list = [
    Time("99d3de6c-66f4-11ea-8ec1-f07960024c26", 'cfa453c4-6838-11ea-b6ff-f07960024c26', 10),
    Time("99d3e164-66f4-11ea-8ec1-f07960024c26", 'cfa45702-6838-11ea-b6ff-f07960024c26', 10),
    Time("99d3e1e6-66f4-11ea-8ec1-f07960024c26", 'cfa457a2-6838-11ea-b6ff-f07960024c26', 10),
    Time("99d3e1e6-66f4-11ea-8ec1-f07960024c26", 'cfa45838-6838-11ea-b6ff-f07960024c26', 10),
    Time("99d3e2a4-66f4-11ea-8ec1-f07960024c26", 'cfa458a6-6838-11ea-b6ff-f07960024c26', 10),
]


@app.route('/time', methods=['GET', 'POST', 'PUT', 'DELETE'])
def trekker_methods():
    if request.method == 'GET':
        get_ifo_list = [i.get_all_info() for i in trekker_list]
        return jsonify(get_ifo_list)
    elif request.method == 'POST':
        get_ifo_list = [i.get_all_info() for i in trekker_list]
        return jsonify(get_ifo_list)
    elif request.method == 'PUT':
        get_ifo_list = [i.get_all_info() for i in trekker_list]
        return jsonify(get_ifo_list)
    elif request.method == 'DELETE':
        get_ifo_list = [i.get_all_info() for i in trekker_list]
        return jsonify(get_ifo_list)


if __name__ == '__main__':
    app.run(debug=True)
