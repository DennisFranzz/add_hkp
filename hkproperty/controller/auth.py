import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


from hkproperty.dao.base_dao import BaseDao
from hkproperty import query_sql, db

bp = Blueprint('auth', __name__, url_prefix='/auth')




@bp.route('/login', methods=('GET', 'POST'))
def login():
    print('[Controller] login')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        dao = BaseDao()
        user_results = dao.excute_query(query_sql.QUERY_FIND_AGENT_BY_USERNAME, {'username': username})
        user = None
        if user_results is None:
            error = 'Incorrect username.'
        else:
            user = user_results[0]
            result_password = user['password']
            print(result_password+' vs '+password)
            if not (result_password == password):
                if check_password_hash(result_password, password):
                    pass
                else:
                    print('a')
                    error = 'Incorrect password.'


        if error is None:
            session.clear()
            session['user_id'] = user['email']
            return redirect(url_for('property.property_list'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        dao = BaseDao()
        g.user = dao.excute_query(
            query_sql.QUERY_FIND_USER_BY_EMAIL, {'email': user_id}
        )[0]


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view