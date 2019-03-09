from sqlalchemy import  create_engine


from models import  *

engine=create_engine('mysql+pymysql://root:123456@localhost:3306/test2_db')

def create_table(table_name):
    table_name.metadata.create_all(engine)

    print('创建成功')