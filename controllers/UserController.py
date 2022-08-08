# pseudo code
from flask import render_template, redirect, url_for, request, abort, flash, jsonify
from models.User import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def list():
    users = User.query.all() 
    result = []   

    for user in users:   
        user_data = {}   
        user_data['public_id'] = user.public_id  
        user_data['name'] = user.name 
        user_data['password'] = user.password
        user_data['admin'] = user.admin 
        
        result.append(user_data)   

    return jsonify({'users': result})

def store():
    ...

def show(userId):
    ...

def update(userId):
    ...

def delete(userId):
    ...