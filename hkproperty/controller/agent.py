import locale

from flask import Blueprint, render_template, request, g, url_for

from hkproperty import query_sql
from hkproperty.controller.auth import agent_required, branch_manager_required
from hkproperty.controller.table import PriceCol
from hkproperty.dao.base_dao import BaseDao
from hkproperty.controller import property
from flask_table import Table, Col, BoolCol, LinkCol, DateCol, DatetimeCol, NestedTableCol

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

@bp.route('/mybranch', methods=['GET'])
@agent_required
def my_branch_page():
    return render_template('agent/mybranch.html', agents = find_agent_by_branch(g.agent['branch_id']))

@bp.route('/mybranch/trans_report', methods=['POST','GET'])
@branch_manager_required
def branch_report():
    table = branch_trans_report(g.agent['branch_id'])
    summary = branch_trans_report_summary(g.agent['branch_id'])
    return render_template('agent/trans_report.html', report=table, summary=summary)


def find_agent_by_branch(id):
    error = None
    dao = BaseDao()
    form_object = {'branch_id':id}
    transaction_results = dao.excute_query(query_sql.QUERY_FIND_AGENT_BY_BRANCH, form_object)
    table = build_agent_table(transaction_results)
    return table


def find_transaction(request):
    error = None
    dao = BaseDao()
    form_type = '%{}%'
    form_type = form_type.format('')
    form_object = {'agent_id':g.agent['agent_id'], 'type':form_type}
    transaction_results = dao.excute_query(query_sql.QUERY_FIND_TRANSACTION_BY_AGENT, form_object)
    table = build_transaction_table(transaction_results)
    return table


def branch_trans_report(branch_id):
    error = None
    dao = BaseDao()
    form_object = {'branch_id':g.agent['branch_id']}
    transaction_results = dao.excute_query(query_sql.QUERY_BRANCH_REPORT, form_object)
    table = build_report_table(transaction_results)
    return table


def branch_trans_report_summary(branch_id):
    error = None
    dao = BaseDao()
    form_object = {'branch_id':g.agent['branch_id']}
    report_results = dao.excute_query(query_sql.QUERY_BRANCH_REPORT_BRANCH_SUMMARY, form_object)

    return report_results

def build_transaction_table(result_dict):
    table = TransactionTable(result_dict)
    return table


def build_report_table(result_dict):
    table = TransReportTable(result_dict)
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



class TransReportAgentTable(Table):
    agent_id = Col('Agent ID')
    name = Col('Agent Name')

class TransReportTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-sm']
    thead_classes = ['thead-dark']
    agent_id = Col('Agent ID')
    name = Col('Agent Name')
    total_count = Col('Total Trans. Count')
    sale_count = Col('Sale Trans. Count')
    total_sold_price = PriceCol('Total Sold Price')
    total_sale_comm = Col('Total Sale Commission')
    rent_count = Col('Rent Trans. Count')
    total_rent_price = Col('Total Rental Price')
    total_rent_comm = Col('Total Rental Commission')


def build_agent_table(result_dict):
    table = AgentTable(result_dict)
    return table


class AgentTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-sm']
    thead_classes = ['thead-dark']
    agent_id = Col('ID')
    name = Col('name')
    email = Col('email')
    phone = Col('phone')


def format_price(text):
    locale.setlocale( locale.LC_ALL, '' )
    text = locale.currency( text, grouping=True )
    return text;