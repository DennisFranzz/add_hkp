import locale

from flask import Blueprint, render_template, request, g, url_for

from hkproperty import query_sql, insert_update_sql
from hkproperty.controller.auth import admin_required
from hkproperty.dao.base_dao import BaseDao
from hkproperty.controller import property
from flask_table import Table, Col, BoolCol, LinkCol, DateCol, DatetimeCol, NestedTableCol


bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=['GET'])
@admin_required
def home():
    return render_template('/base.html')

@bp.route('/users', methods=['GET'])
@admin_required
def user_list():
    return render_template('/admin/userlist.html')


@bp.route('/users/filter', methods=['GET'])
@admin_required
def user_list_filter():
    return find_user(request)


@bp.route('/properties', methods=['GET'])
@admin_required
def property_list():
    trans_type_list = property.list_trans_type()
    return render_template('admin/property_list.html', trans_types=trans_type_list)


@bp.route('/properties/filter', methods=['GET'])
@admin_required
def property_list_filter():
    if len(request.args) >0:
        result_table = property.find_property(request, True)
        return result_table.__html__()
    else:
        return


@bp.route('/properties/maintain', methods=['GET', 'POST'])
@admin_required
def maintain_property():
    return


@bp.route('/properties/delete', methods=[ 'POST'])
@admin_required
def delete_property():
    return


def find_user(request):
    error = None
    dao = BaseDao()
    form_value = {}

    form_id = '%{}%'
    if request.args.get('id')is None:
        form_id = form_id.format('')
        form_value['id'] = ''
    else:
        form_id = form_id.format(request.args.get('id'))
        form_value['id'] = request.args.get('id')

    form_username = '%{}%'
    if request.args.get('username')is None:
        form_username = form_username.format('')
        form_value['username'] = ''
    else:
        form_username = form_username.format(request.args.get('username'))
        form_value['username'] = request.args.get('username')

    form_usergroup = '%{}%'
    if request.args.get('usergroup')is None:
        form_usergroup = form_usergroup.format('')
        form_value['usergroup'] = ''
    else:
        form_usergroup = form_usergroup.format(request.args.get('usergroup'))
        form_value['usergroup'] = request.args.get('usergroup')
    form_object = {'id':form_value['id'], 'username':form_value['username'],
        'usergroup':form_value['usergroup']}
    results = dao.excute_query(query_sql.QUERY_FIND_ALL_USER, form_object)
    table = build_table(results)
    return table.__html__()



@bp.route('/users/maintain', methods=['GET', 'POST'])
@admin_required
def maintain_user():
    dao = BaseDao()
    error = None
    if request.method == 'POST':
        id = request.form['user_id']
        if id =='':
            last_id_result = dao.excute_query(query_sql.QUERY_FIND_LAST_USER_ID)
            id = last_id_result[0]['id'] +1

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


@bp.route('/users/delete', methods=[ 'POST'])
@admin_required
def delete_user():
    dao = BaseDao()
    id = request.form['id']
    params = {'id':id}
    result = dao.excute_upsert(insert_update_sql.DELETE_HKPUSER, params)
    return str(result.rowcount)


class UserTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-sm']
    thead_classes = ['thead-dark']
    id = Col('ID',column_html_attrs={'class': 'col-id'})
    username = Col('Username')
    usergroup = Col('Usergroup')
    update = LinkCol('Update', 'admin.maintain_user', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'admin.delete_user', column_html_attrs={'class': 'delete'})


def build_table(result_dict):
    table = UserTable(result_dict)
    return table

