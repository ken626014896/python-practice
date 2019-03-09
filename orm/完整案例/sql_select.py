#coding:utf-8

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import *

def select(table_name):
    engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test2_db")
    print ("初始化数据库引擎")

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    print ("创建session对象")

    table_data = session.query(table_name).all()
    print ("查询")

    session.close()

    return table_data


if __name__ == "__main__":
  pass