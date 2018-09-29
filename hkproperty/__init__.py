import os

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy as sa
from sqlalchemy import create_engine
from hkproperty import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    POSTGRES = {
        'user': 'postgres',
        'pw': 'postgres',
        'db': 'hkproperty2',
        'host': 'localhost',
        'port': '5432',
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

    #print(app.config['SQLALCHEMY_DATABASE_URI'])
    #db = SQLAlchemy(app)

    db.create_db(app)




    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
