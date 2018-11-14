from flask import Blueprint, render_template, request, g, url_for

from hkproperty import query_sql
from hkproperty.dao.base_dao import BaseDao
from hkproperty.controller import property
from flask_table import Table, Col, BoolCol, LinkCol

bp = Blueprint('agent', __name__)

@bp.route('/', methods=['GET'])
@agent_required
def agent_home():
    return render_template('agent/home.html')


@bp.route('/transaction', methods=['GET']
@agent_required
def transaction_list_filter():
    if len(request.args) >0:
        result_table = find_transaction(request)
        return result_table.__html__()
    else:
        return


def find_transaction(request):
    error = None
    dao = BaseDao()
    form_type = '%{}%'
    form_type = form_type.format('')
    form_object = {'agent_id':g.agent['agent_id'], 'type':form_type}
    transaction_results = dao.excute_query(query_sql.QUERY_FIND_TRANSACTION_BY_AGENT, form_object)
    table = build_table(transaction_results)
    return table
