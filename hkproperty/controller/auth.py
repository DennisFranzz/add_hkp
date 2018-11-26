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
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        dao = BaseDao()
        user_results = dao.excute_query(query_sql.QUERY_FIND_USER_BY_USERNAME, {'username': username})
        agent_result = dao.excute_query(query_sql.QUERY_FIND_AGENT_BY_USERNAME, {'username': username})
        user = None
        agent = None
        if user_results is None or len(user_results) == 0:
            error = 'Incorrect username or password.'
        else:
            user = user_results[0]
            result_password = user['password']
            print(result_password+' vs '+password)
            if not (result_password == password):
                if check_password_hash(result_password, password):
                    pass
                else:
                    error = 'Incorrect username or password.'


        if error is None:

            session.clear()
            session['user_id'] = user['id']
            if agent_result is not None and len(agent_result)>0:
                agent = agent_result[0]
                if agent is not None:
                    session['agent_id'] = agent['agent_id']
            if user['usergroup'] == 'admin':
                return redirect(url_for('admin.home'))
            else:
                return redirect("/")

        flash(error)

    return render_template('auth/login.html', error=error)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    agent_id = session.get('agent_id')

    if user_id is None:
        g.user = None
    else:
        dao = BaseDao()
        g.user = dao.excute_query(
            query_sql.QUERY_FIND_USER_BY_ID, {'id': user_id}
        )[0]

    if agent_id is None:
        g.agent = None
    else:
        dao = BaseDao()
        g.agent = dao.excute_query(
            query_sql.QUERY_FIND_AGENT_BY_ID, {'id': agent_id}
        )[0]


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

def agent_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        else:
            if g.agent is None:
                return render_template('error.html', error_message='You are not an agent')

            else:
                return view(**kwargs)
    return wrapped_view

def branch_manager_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        else:
            if  g.user['usergroup'] != 'branch_manager':
                return render_template('error.html', error_message='You are not a branch manager')
            else:
                return view(**kwargs)
    return wrapped_view

def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        else:
            if g.user['usergroup'] != 'admin':
                return render_template('error.html', error_message='You are not Admin')
            else:
                return view(**kwargs)
    return wrapped_view