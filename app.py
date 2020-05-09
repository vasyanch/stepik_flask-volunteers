from flask import Flask
from flask_migrate import Migrate

from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


from views import post_help, get_streets, get_districts, get_volunteers

if __name__ == '__main__':
    app.run()
