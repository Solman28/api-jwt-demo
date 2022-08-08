from db import db

class User(db.Model):
     __tablename__ = 'users'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50))
     password = db.Column(db.String(100))
     admin = db.Column(db.Boolean)
     public_id = db.Column(db.String(100))
     
     @property
     def serialize(self):
          return {
               'id': self.id,
               'name': self.name,
               'password': self.password,
               'admin': self.admin,
               'public_id': self.public_id,
          }

     def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

     def delete_user(self):
          db.session.delete(self)
          try:
               db.session.commit()
          except Exception as e:
               db.session.rollback()
               db.session.flush()
               print(e)

     @classmethod
     def getUser(cls, id=None, name=None, public_id=None):
          if id:
               return cls.query.filter_by(id=id).first()
          if name:
               return cls.query.filter_by(name=name).first()
          if public_id:
               return cls.query.filter_by(public_id=public_id).first()