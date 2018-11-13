from flask import Blueprint, render_template, request, g

from hkproperty import query_sql
from hkproperty.dao.base_dao import BaseDao
from flask_table import Table, Col, BoolCol

bp = Blueprint('property', __name__)


@bp.route('/', methods=['GET'])
@bp.route('/property', methods=['GET'])
def property_list():

    trans_type_list = list_trans_type()
    if len(request.args) >0:
        result_table = find_property(request);
        return render_template('property/property_list.html', table=result_table, trans_types=trans_type_list)
    else:
        return render_template('property/property_list.html', trans_types=trans_type_list)


def find_property(request):
    form_value ={}

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
    table = build_table(property_results)
    return table


def list_trans_type():
    dao = BaseDao()
    results = dao.excute_query(query_sql.QUERY_LIST_TRANSACTION_TYPE)
    return results


def build_table(result_dict):
    table = ItemTable(result_dict)
    return table


class ItemTable(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover', 'table-sm']
    thead_classes = ['thead-dark']
    district = Col('District')
    estate = Col('Estate')
    block = Col('Block')
    floor = Col('Floor')
    flat = Col('Flat')
    area = Col('Gross area sq. ft.')
    bedrooms = Col('Bedrooms')
    hascarpark = BoolCol('Provide Car Park', yes_display='Y', no_display='N')
    selling_price = Col('Selling Price')
    rental_price = Col('Rental Price')
    for_transaction_type = Col('Transaction Type')
    owner = Col('Owner')


class Item(object):
    def __init__(self, district, estate):
        self.district = district
        self.estate = estate