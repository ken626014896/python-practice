a=[[1,5,8],[1,4,2],[3,6,9]]


b=[y for  x  in a for y in x]
b2=map(lambda x:x ,b)
print(b2)
for i  in b2:
    print(i)
print(b)



def quickSort(alist):

    if len(alist)<=1:
        return alist
    min=len(alist)//2
    midnum = alist[min]

    smalllist = [i for i in alist[:min] if i <= midnum ]+[i for i in alist[min+1:] if i <= midnum ]

    biglist =[i for i in alist[:min] if i > midnum ]+[i for i in alist[min+1:] if i > midnum ]
    lastlsit = quickSort(smalllist) + [midnum] + quickSort(biglist)

    return lastlsit

print(quickSort(b))

