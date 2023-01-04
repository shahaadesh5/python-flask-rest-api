from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import uuid

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

users = []

@app.route('/user', methods=['GET', 'POST'])
@cross_origin()
def user():
    global users
    if request.method == 'GET':
        return users
    if request.method == 'POST':
        user_request = request.json
        if user_request.get('email') == None or user_request.get('name') == None:
            return Response('{"message": "Email or Name missing"}', status=400, mimetype='applicaiton/json')
        user_request['id'] = uuid.uuid4()
        users.append(user_request)
        return Response('{"message": "User created"}', status=201, mimetype='applicaiton/json')

if __name__ == "__main__":
    app.run(debug=True)