from flask import Blueprint, render_template, request, g, url_for

from hkproperty import query_sql
from hkproperty.controller.auth import agent_required
from hkproperty.dao.base_dao import BaseDao
from hkproperty.controller import property
from flask_table import Table, Col, BoolCol, LinkCol, DateCol, DatetimeCol

bp = Blueprint('agent', __name__)

@bp.route('/', methods=['GET'])
@agent_required
def agent_home():
    return render_template('agent/home.html')


@bp.route('/transaction', methods=['GET'])
@agent_required
def transaction_list_filter():
    result_table = find_transaction(request)
    return result_table.__html__()

@branch_manager_required
def my_branch_page():
    return


def find_transaction(request):
    error = None
    dao = BaseDao()
    form_type = '%{}%'
    form_type = form_type.format('')
    form_object = {'agent_id':g.agent['agent_id'], 'type':form_type}
    transaction_results = dao.excute_query(query_sql.QUERY_FIND_TRANSACTION_BY_AGENT, form_object)
    table = build_transaction_table(transaction_results)
    return table


def build_transaction_table(result_dict):
    table = TransactionTable(result_dict)
    return table


class TransactionTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-sm']
    thead_classes = ['thead-dark']
    ref_no = Col('#')
    type = Col('Type')
    transaction_date = DatetimeCol('Transaction Date', datetime_format='yyyy-MM-dd HH:mm')
    property_id = Col('Property')
    sold_price = Col('Sold Price')
    rental_price = Col('Rental Price')
    customer_id = Col('Customer')
    commission = Col('Commission')
