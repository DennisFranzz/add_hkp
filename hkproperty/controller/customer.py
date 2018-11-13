from flask import Blueprint, render_template, request, g

from hkproperty import query_sql
from hkproperty.dao.base_dao import BaseDao
from flask_table import Table, Col, BoolCol

bp = Blueprint('customer', __name__)

@bp.route('/customer', methods=['GET'])
def customer_list():
    if len(request.args) >0:
        result_table = find_customer(request);
        return render_template('customer/customer_list.html', table=result_table)
    else:
        return render_template('customer/customers_list.html')
		
def customer_details():

	return

		
def find_customer(request):
    form_value ={}

    form_id = '%{}%'
    if request.args.get('id')is None:
        form_id = form_id.format('')
        form_value['id'] = ''
    else:
        form_id = form_id.format(request.args.get('id'))
        form_value['id'] = request.args.get('id')

    form_name = '%{}%'
    if request.args.get('estate')is None:
        form_name = form_name.format('')
        form_value['name'] = ''
    else:
        form_name = form_name.format(request.args.get('name'))
        form_value['name'] = request.args.get('name')

    form_phone = '%{}%'
    if request.args.get('phone')is None:
        form_phone = form_phone.format('')
		form_value['phone'] = ''
    else:
        form_phone = form_phone.format(request.args.get('phone'))
        form_value['phone'] = request.args.get('phone')

    error = None
    dao = BaseDao()
    form_object = {'id': form_id, 'name': form_name,'phone': form_phone}

    g.form_value = form_value
    property_results = dao.excute_query(query_sql.QUERY_FIND_CUSTOMER, form_object)
    table = build_table(property_results)
    return table
	
	
def build_table(result_dict):
    table = ItemTable(result_dict)
    return table


class ItemTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-sm']
    thead_classes = ['thead-dark']
    id = Col('ID')
	title = Col('Title')
    name = Col('Name')
    phone = Col('Phone')
    details = LinkCol('Details', 'details', url_kwargs=dict(id='id'))