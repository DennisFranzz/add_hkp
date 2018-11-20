from flask import Blueprint, render_template, request, g

from hkproperty import query_sql
from hkproperty.controller.table import PriceCol

from hkproperty.dao.base_dao import BaseDao
from flask_table import Table, Col, BoolCol, LinkCol

bp = Blueprint('property', __name__)



@bp.route('/property', methods=['GET'])
def property_list():
    trans_type_list = list_trans_type()
    return render_template('property/property_list.html', trans_types=trans_type_list)


@bp.route('/property/filter', methods=['GET'])
def property_list_filter():
    if len(request.args) >0:
        result_table = find_property(request, False)
        return result_table.__html__()
    else:
        return

def find_property(request, isAdmin):
    form_value = {}

    form_estate = '%{}%'
    if request.args.get('estate')is None:
        form_estate = form_estate.format('')
        form_value['estate'] = ''
    else:
        form_estate = form_estate.format(request.args.get('estate'))
        form_value['estate'] = request.args.get('estate')

    form_district = '%{}%'
    if request.args.get('district')is None:
        form_district = form_district.format('')
        form_value['district'] = ''
    else:
        form_district = form_district.format(request.args.get('district'))
        form_value['district'] = request.args.get('district')

    form_owner_name = '%{}%'
    if request.args.get('owner')is None:
        form_owner_name = form_owner_name.format('')
        form_value['owner'] = ''
    else:
        form_owner_name = form_owner_name.format(request.args.get('owner'))
        form_value['owner'] = request.args.get('owner')

    form_type = request.args.get('type')
    if form_type is None:
        form_type = 'both'
    form_value['type'] = request.args.get('type')

    error = None
    dao = BaseDao()
    form_object = {'estate': form_estate, 'district': form_district,
                   'type': form_type, 'owner_name': form_owner_name}

    g.form_value = form_value
    property_results = dao.excute_query(query_sql.QUERY_FIND_PROPERTY, form_object)
    if isAdmin:
        table = build_admin_table(property_results)
    else:
        table = build_table(property_results)
    return table


def list_trans_type():
    dao = BaseDao()
    results = dao.excute_query(query_sql.QUERY_LIST_TRANSACTION_TYPE)
    return results


def find_property_owner():
    dao = BaseDao()
    results = dao.excute_query(query_sql.QUERY_FIND_PROPERTY_OWNER)
    return results


def build_table(result_dict):
    table = PropertyTable(result_dict)
    return table


def build_admin_table(result_dict):
    table = AdminPropertyTable(result_dict )
    return table

class PropertyTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-sm']
    thead_classes = ['thead-dark']
    property_id = Col('ID')
    district = Col('District')
    estate = Col('Estate')
    block = Col('Block')
    floor = Col('Floor')
    flat = Col('Flat')
    area = Col('Gross area sq. ft.')
    bedrooms = Col('Bedrooms')
    hascarpark = BoolCol('Provide Car Park', yes_display='Y', no_display='N')
    selling_price = PriceCol('Selling Price', column_html_attrs={'class': 'price'})
    rental_price = PriceCol('Rental Price', column_html_attrs={'class': 'price'})
    for_transaction_type = Col('Transaction Type')
    owner = Col('Owner')


class AdminPropertyTable(PropertyTable):
    update = LinkCol('Update', 'admin.maintain_property', url_kwargs=dict(id='property_id'))
    delete = LinkCol('Delete', 'admin.delete_property', column_html_attrs={'class': 'delete'})
