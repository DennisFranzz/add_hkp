import os

from flask import Flask

from hkproperty import db
from hkproperty.config import Config


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    #app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.SQLALCHEMY_DATABASE_URI

    #print(app.config['SQLALCHEMY_DATABASE_URI'])
    #db = SQLAlchemy(app)






    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('hkproperty.config.DevelopmentConfig')
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

    from . import db
    db.init_app(app)

    from hkproperty.controller import auth,property
    app.register_blueprint(auth.bp)
    app.register_blueprint(property.bp)

    #app.add_url_rule('/', endpoint='property_list')
    return app
