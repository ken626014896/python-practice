from models import *
from sql_create import create_table
from sql_insert import  insert
from  sql_select import  select

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


a=input('1，创建表；2，插入数据；3，查询数据')
if a=='1':
    create_table(Phone)
    create_table(Company)
elif a=='2':
    companys = {
        "Apple": "Amercian",
        "Xiaomi": "China",
        "Huawei": "China",
        "Sungsum": "Korea",
        "Nokia": "Finland"
    }

    phones = (
        [1, "iphoneX", "Apple", 8400],
        [2, "xiaomi2s", "Xiaomi", 3299],
        [3, "Huaweimate10", "Huawei", 3399],
        [4, "SungsumS8", "SungSum", 4099],
        [5, "NokiaLumia", "Nokia", 2399],
        [6, "iphone4s", "Apple", 3800]
    )

    for key in companys:
        new_company = Company(name=key, location=companys[key])
        insert(new_company)

    for phone in phones:
        id = phone[0]
        model = phone[1]
        company_name = phone[2]
        price = phone[3]

        new_phone = Phone(id=id, model=model, company_name=company_name, price=price)
        insert(new_phone)

elif a=='3':
    engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test2_db")
    print("初始化数据库引擎")
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    a=session.query(Company).filter_by(name = "Apple").first()
    for i in a.phone_of_company:
       print(i.price)


