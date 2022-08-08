# pseudo code
from flask import redirect, url_for, request, jsonify
from models.User import User
from models.Author import Author

from werkzeug.security import generate_password_hash
import uuid

from routes.decorators import token_required

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


@token_required
def list(current_user, public_id):
    authors = Author.query.all()   

    output = []  

    for author in authors:   
        author_data = {}
        author_data['name'] = author.name 
        author_data['book'] = author.book 
        author_data['country'] = author.country  
        author_data['booker_prize'] = author.booker_prize
        output.append(author_data)  

    return jsonify({'list_of_authors' : output})

@token_required
def create(current_user):
    data = request.get_json()  

    if 'name' not in data or 'book' not in data or 'country' not in data:
        return jsonify({'message': 'you must send data name, book, country'}) 
    else:
        new_author = Author(
            name=data['name'], 
            book=data['book'], 
            country=data['country'], 
            booker_prize=False,
            user_id=current_user.id
        ) 
        new_author.save_to_db() 

        return jsonify({'message': 'registered successfully'}) 

@token_required
def delete(current_user, name):
    author = Author.getAuthor(name=name, user_id=current_user.id)
    if not author:   
       return jsonify({'message': 'author does not exist'})   

    author.delete_author()

    return jsonify({'message': 'Author deleted'})