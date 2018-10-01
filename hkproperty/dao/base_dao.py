

from flask import current_app
from sqlalchemy import text

from hkproperty import db


class BaseDao:
    def result_proxy_to_list(self, result_proxy):
        result_list = [];
        for row in result_proxy:
            row_as_dict = dict(row)
            result_list.append(row_as_dict)

        return result_list

    def excute_query(self, sql, params):
        engine = db.get_db()
        statement = text(sql)
        result_proxy = engine.execute(statement, params)
        result_list = self.result_proxy_to_list(result_proxy)
        return result_list
