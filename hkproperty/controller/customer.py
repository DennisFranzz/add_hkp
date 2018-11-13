from flask import Blueprint, render_template, request, g, url_for

from hkproperty import query_sql
from hkproperty.dao.base_dao import BaseDao
from hkproperty.controller import property
from flask_table import Table, Col, BoolCol, LinkCol

bp = Blueprint('customer', __name__)


@bp.route('/customer', methods=['GET'])
def customer_list():
    return render_template('customer/customer_list.html')


@bp.route('/customer/filter', methods=['GET'])
def customer_list_filter():
    if len(request.args) >0:
        result_table = find_customer(request)
        return result_table.__html__()
    else:
        return


@bp.route('/customer/<int:id>/', methods=['GET'])
def customer_details(id):
    error = None
    customer_result = find_customer_by_id(id)
    if customer_result is None:
        error = 'Innalid customer id.'
    else:
        customer = customer_result[0]

    if error is None:
        preference_id = customer['preference_id']
        if preference_id is not None:
            property_results = find_property_by_preference(preference_id)
            property_table = property.build_table(property_results)
            return render_template('customer/customer_details.html', property_table=property_table, customer=customer)
        else:
            return render_template('customer/customer_details.html', customer=customer)
    else:
        #todo error handle
        return error


def find_customer(request):
    form_value = {}

    form_id = '%{}%'
    if request.args.get('id') is None:
        form_id = form_id.format('')
        form_value['id'] = ''
    else:
        form_id = form_id.format(request.args.get('id'))
        form_value['id'] = request.args.get('id')

    form_name = '%{}%'
    if request.args.get('name') is None:
        form_name = form_name.format('')
        form_value['name'] = ''
    else:
        form_name = form_name.format(request.args.get('name'))
        form_value['name'] = request.args.get('name')

    form_phone = '%{}%'
    if request.args.get('phone') is None:
        form_phone = form_phone.format('')
        form_value['phone'] = ''
    else:
        form_phone = form_phone.format(request.args.get('phone'))
        form_value['phone'] = request.args.get('phone')

    error = None
    dao = BaseDao()
    form_object = {'id': form_id, 'name': form_name,'phone': form_phone}

    g.form_value = form_value
    customer_results = dao.excute_query(query_sql.QUERY_FIND_CUSTOMER, form_object)
    table = build_customer_table(customer_results)
    return table


def find_customer_by_id(customer_id):
    dao = BaseDao()
    form_object = {'id': customer_id}
    customer_results = dao.excute_query(query_sql.QUERY_FIND_CUSTOMER_BY_ID, form_object)
    return customer_results


def find_property_by_preference(pref_id):
    dao = BaseDao()
    form_object = {'prefId': pref_id}
    property_results = dao.excute_query(query_sql.QUERY_FIND_PROPERTY_BY_PREFERENCE, form_object)
    return property_results


def build_customer_table(result_dict):
    table = CustomerTable(result_dict)
    return table


class CustomerTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-sm']
    thead_classes = ['thead-dark']
    id = Col('ID')
    title = Col('Title')
    name = Col('Name')
    phone = Col('Phone')
    details = LinkCol('Details', 'customer.customer_details', url_kwargs=dict(id='id'))
