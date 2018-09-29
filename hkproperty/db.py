from flask import current_app
from sqlalchemy import create_engine


def create_db(app):
    with app.app_context():
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        if database_is_empty(engine):
            with current_app.open_resource('schema.sql') as f:
                engine.execute(f.read().decode('utf8'))




def database_is_empty(engine):
    table_names = engine.table_names()
    is_empty = table_names == []
    print('Db is empty: {}'.format(is_empty))
    return is_empty
