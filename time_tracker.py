from flask import Flask
from flask import jsonify
from flask import request
from flask_api import status
from uuid import uuid1

app = Flask(__name__)


class Time:
    def __init__(self, per_id, pro_id, time):
        self.per_id = per_id
        self.pro_id = pro_id
        self.time = time

    def per_id(self):
        return jsonify(self.per_id)

    def pro_id(self):
        return jsonify(self.pro_id)

    def time(self):
        return jsonify(self.time)

    def get_all_info(self):
        return {[self.per_id, self.pro_id]: self.time}


trekker_list = [
    Time(10000001, 11111111, 10),
    Time(10000001, 11111111, 10),
    Time(10000001, 11111111, 10),
    Time(10000001, 11111111, 10),
    Time(10000001, 11111111, 10),
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
