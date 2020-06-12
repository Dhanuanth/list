
list_1=[]

list_1=[int(ele) for ele in input('enter the elements in list1(seperated by spaces): ').split() ] # enter the elements seperated by spaces
i=0
while(i<len(list_1)):
    if list_1[i]<0:
        list_1.remove(list_1[i])
    else:
        i+=1
print(*list_1,sep=',')
#############
list_2=[]

list_2=[int(ele) for ele in input('enter the elements in list2(seperated by spaces): ').split() ]# enter the elements seperated by spaces
i=0
while(i<len(list_2)):
    if list_2[i]<0:
        list_2.remove(list_2[i])
    else:
        i+=1
print(list_2)

