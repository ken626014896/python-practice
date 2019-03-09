# coding:utf-8

from sqlalchemy import Column, CHAR, INTEGER,String,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import  relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(CHAR(20), primary_key=True)
    name = Column(CHAR(20))


class Solary(Base):
    __tablename__ = "solary"

    id = Column(INTEGER, primary_key=True)
    name = Column(CHAR(20))
    num = Column(CHAR(20))


#一对多
class Company(Base):
    __tablename__ = "company"

    name = Column(String(20), primary_key=True)
    location = Column(String(20))

    def __repr__(self):
        return "name:{0} location:{1}".format(self.name, self.location)


class Phone(Base):
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True)
    model = Column(String(32))
    price = Column(String(32))
    company_name = Column(String(32), ForeignKey("company.name"))
    company = relationship("Company", backref="phone_of_company")

    def __repr__(self):
        return "{0} model:{1},sales:{2} sales:{3} price:{4}".format(self.id, self.model, self.sales, self.price)

    # 表明将phone表和Company表联系在一起。backref是反向关联，使用规则是：
    #
    # 查询phone表，返回phone_obj，可以通过phoen_obj.Company查询到company中外键关联的数据。这个称之为：正向查询。
    # 查询company表，返回company_obj，可以通过company_obj.phone_of_company查询到phone表的外键关联数据。这个称之为：反向查询。