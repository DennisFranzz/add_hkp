from flask import current_app
from sqlalchemy import  text

from hkproperty import db, query_sql
from hkproperty.dao.base_dao import BaseDao


class PropertyDao(BaseDao):
    def find_property_for_sale(self):
        return self.excute_query(query_sql.QUERY_FIND_PROPERTY_BY_TRANS_TYPE,
                                 {"trans_type": 'sale'})

    def find_property_for_rent(self):
        return self.excute_query(query_sql.QUERY_FIND_PROPERTY_BY_TRANS_TYPE,
                             {"trans_type": 'rent'})

    def find_property_for_sale_or_rent(self):
        return self.excute_query(query_sql.QUERY_FIND_PROPERTY_BY_TRANS_TYPE,
                                 {"trans_type": 'both'})

