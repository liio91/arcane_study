from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return jsonify("get")
    elif request.method == 'POST':
        return jsonify("post")


class ApiTest(Resource):
    def get(self):
        return {"test": 'test'}

    def post(self):
        body = request.get_json()
        return {"body": body}, 201


api.add_resource(ApiTest, '/api/')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
