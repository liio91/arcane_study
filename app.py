from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return jsonify("get")
    elif request.method == 'POST':
        return jsonify("post")


if __name__ == '__main__':
    app.run(debug=True, port=4000)
