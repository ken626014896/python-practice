
def get_result(tlist):
   hint=[0]
   for i in range(1,len(tlist)):
       if  tlist[i-1]>tlist[i]:
           hint.append(i-1)
   hint.append(len(tlist)-1)

   max_num=0
   for i in range(1,len(hint)):

        temp=tlist[hint[i]]-tlist[hint[i-1]]
        if temp>max_num:
            max_num=temp
        hint[i]+=1

   return  max_num



temperature_list=[21, 28, 26, 29, 31, 28, 29]

print(get_result(temperature_list))

