# pseudo code
from flask import request, make_response, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
import uuid

from models.User import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def login():
    auth = request.authorization   

    if not auth or not auth.username or not auth.password:  
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})    

    user = User.query.filter_by(name=auth.username).first()

    if check_password_hash(user.password, auth.password):  
        token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'], algorithm="HS256")  
        return jsonify({'token' : token }) 

    return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})


def register():
    data = request.get_json()

    if 'name' not in data or 'password' not in data:
        return jsonify({'message': 'you must send data name, password'}) 
    else:
        print(data)
        hashed_password = generate_password_hash(data['password'], method='sha256')

        new_user = User(
            public_id=str(uuid.uuid4()), 
            name=data['name'], 
            password=hashed_password, 
            admin=False
        ) 
        new_user.save_to_db()

        return jsonify({'message': 'registered successfully'}) 
