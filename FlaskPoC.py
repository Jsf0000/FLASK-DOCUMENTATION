from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'You made a GET request'
    elif request.method == 'POST':
        return 'You made a POST request'
    return "Hello World"

@app.route('/make_response')
def response():
    response = make_response()
    response.status_code = 202
    response.headers['content-type'] = 'application/json'
    return response
@app.route('/status', methods=['GET'])
def status():
    return 'status', 200


@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

#Type Dinamic

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1+number2}"

#query parameters
@app.route('/handle_url_params')
def handle_params():
    a = request.args['a']
    b = request.args['b']
    return f'{a} , {b}'




# if __name__ == '__main__':
#     app.run(host='0.0.0.1', debug=True)

