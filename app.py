from flask import Flask
from flask_migrate import Migrate

from routes.user_bp import user_bp
from routes.auth_bp import auth_bp
from routes.author_bp import author_bp

from db import db

app = Flask(__name__)
app.config.from_object('config')

app.url_map.strict_slashes = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(author_bp, url_prefix='/author')


if __name__ == '__main__':
    app.debug = True
    app.run()