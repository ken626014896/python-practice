import  random
import itertools

def  result(n):
    num_list=list(range(1,7))
    b=[]
    d={}
    for i in itertools.combinations_with_replacement(num_list, 6):
        total=sum(i)
        if total not in d.keys():
           d[total]=1
        else:
            d[total]+=1
        b.append(i)

    print(b)
    print('总长度为',len(b))
    print(d)

    for i,j in d.items():
        print(f'和为{i}，出现的概率{j/sum(d.values())}')
result(6)
