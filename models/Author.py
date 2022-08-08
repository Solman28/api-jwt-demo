from db import db
from sqlalchemy import and_

class Author(db.Model):
     __tablename__ = 'authors'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), unique=True, nullable=False)
     book = db.Column(db.String(20), unique=True, nullable=False)
     country = db.Column(db.String(50), nullable=False)
     booker_prize = db.Column(db.Boolean)
     user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

     @property
     def serialize(self):
          return {
               'id': self.id,
               'name': self.name,
               'book': self.book,
               'country': self.country,
               'booker_prize': self.booker_prize,
               'user_id': self.user_id
          }

     def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

     def delete_author(self):
          db.session.delete(self)
          try:
               db.session.commit()
          except Exception as e:
               db.session.rollback()
               db.session.flush()
               print(e)
     
     @classmethod
     def getAuthor(cls, name=None, user_id=None):
          return cls.query.filter(and_(name==name, user_id==user_id)).first()