from flask import current_app
from sqlalchemy import  text

from hkproperty import db
from hkproperty.dao.base_dao import BaseDao


class AgentDao(BaseDao):
    def find_agent_by_username(username):
        engine = db.get_db()
        statement = text("Select * from agent where username = :username;")
        result_proxy = engine.execute(statement,
                                                    {"username":username})
        result_list = BaseDao.result_proxy_to_list(result_proxy)
        return result_list
