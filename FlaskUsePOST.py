from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')
app.debug = True


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        print(username, password)
        return f"{username}, {password}"

@app.route('/handle_json', methods=['POST'])
def handle_json():
    a = request.json['a']
    b = request.json['b']

    return jsonify({'message': a, 'value': b})


