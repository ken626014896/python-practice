from sqlalchemy import  Column ,String,Integer,create_engine

from sqlalchemy.orm import  sessionmaker
import pymysql
from sqlalchemy.ext.declarative import declarative_base

#创建基类
Base=declarative_base()

#定义 类
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    # 初始化数据库连接:


engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test2_db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id=2, name=u'Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()
# print('添加数据成功')

#查询
session=DBSession()
a=session.query(User).all()
for i in  a:
    print(i.id)
session.close()
