from flask import Flask, jsonify, request
import dbActions

# Init app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({ 'msg' : 'Hello World!' })


@app.route('/defibrillators', methods=['GET', 'POST'])
def defibrillators():
    if (request.method == 'GET'):
        defibrillatorsList = dbActions.returnDefibrillators()

        return jsonify({'defibrillatorsList' : defibrillatorsList })

    elif (request.method == 'POST'):
        httpCode = dbActions.createDefibrillator(request.json['lat'], request.json['long'], request.json['name'],
                                                 request.json['description'], request.json['problemType'],
                                                 request.json['problemDescription'], request.json['photo'])
        return httpCode


@app.route('/createUser', methods=['POST'])
def create_user():
    if (request.method == 'POST'):
        httpCode = dbActions.createUser(request.json['username'], request.json['password'], request.json['userType'])

        return httpCode


@app.route('/login', methods=['POST'])
def login():
    if (request.method == 'POST'):
        result = dbActions.login(request.json['username'], request.json['password'], request.json['userType'])

        return result


@app.route('/updateDefibrillator', methods=['PUT'])
def updateDefibrillator():
    if (request.method == 'PUT'):
        if(request.is_json):

            lat = request.json.get('lat', None)
            long = request.json.get('long', None)
            name = request.json.get('name', None)
            description = request.json.get('description', None)
            problemType = request.json.get('problemType', None)
            problemDescription = request.json.get('problemDescription', None)
            photo = request.json.get('photo', None)

            result = dbActions.updateDefibrillator(lat, long, name, description, problemType, problemDescription, photo)

            return result


# Run Server
if __name__ == '__main__':
    app.run(debug=True)






