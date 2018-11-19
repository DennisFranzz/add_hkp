import locale

from flask import Blueprint, render_template, request, g, url_for

from hkproperty import query_sql, insert_update_sql
from hkproperty.controller.auth import admin_required
from hkproperty.dao.base_dao import BaseDao
from hkproperty.controller import property
from flask_table import Table, Col, BoolCol, LinkCol, DateCol, DatetimeCol, NestedTableCol


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/user', methods=['GET', 'POST'])
@admin_required
def maintain_user():
    dao = BaseDao()
    error = None
    if request.method == 'POST':
        id = request.form['user_id']
        if id =='':
            id = 'DEFAULT';

        username = request.form['username']
        password = request.form['password']
        usergroup = request.form['usergroup']
        params = {'id':id,
                  'username':username,
                  'password':password,
                  'usergroup':usergroup}
        result = dao.excute_upsert(insert_update_sql.UPSERT_USER, params)
        return str(result.rowcount)
    else:
        user_id = request.args.get('id')
        user = None
        if user_id is not None:
            user = dao.excute_query(
                query_sql.QUERY_FIND_USER_BY_ID, {'id': user_id}
            )[0]
        return render_template('admin/user.html', user=user)


