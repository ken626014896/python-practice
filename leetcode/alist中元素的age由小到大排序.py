alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
def sort_by_age(list1):

    return sorted(list1,key=lambda x:x['age'])

print(sort_by_age(alist))