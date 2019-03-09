from  models import  User,Solary
from sql_create import create_table
from sql_insert import  insert
from  sql_select import  select


a=input('1，创建表；2，插入数据；3，查询数据')

if a=='1':
    create_table(User)
    create_table(Solary)
elif a=='2':
    new_user=User(id='1',name='ken')
    insert(new_user)
    new_user = User(id='2', name='sam')
    insert(new_user)
    new_user = User(id='3', name='jyp')
    insert(new_user)
elif a=='3':
    a=select(User)
    for i  in  a:
        print('id=%s  name=%s'%(i.id,i.name))