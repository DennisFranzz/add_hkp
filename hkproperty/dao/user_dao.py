from flask import current_app
from sqlalchemy import  text

from hkproperty import db
from hkproperty.dao.base_dao import BaseDao


class UserDao(BaseDao):
    def find_user_by_username(username, is_super_user):
        engine = db.get_db()
        statement = text("Select * from hkpUser where username = :username and is_superuser = :is_superuser;")
        result_proxy = engine.execute(statement,
                                                    {"username":username, "is_superuser": is_super_user})
        result_list = BaseDao.result_proxy_to_list(result_proxy)
        return result_list
