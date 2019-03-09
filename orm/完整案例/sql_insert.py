# coding:utf-8

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER, CHAR
from sqlalchemy import create_engine, Column


def insert(new_data):
    Base = declarative_base()
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test2_db')
    print("创建数据库引擎")

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    print("创建session对象")

    session.add(new_data)
    print("添加数据到session")

    session.commit()
    print("提交数据到数据库")

    session.close()
    print("关闭数据库连接")


if __name__ == "__main__":
    pass