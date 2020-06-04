list_1=[]
n=int(input("enter number of elements in the list :"))
print('enter the elements')
for i in range(n):

    x=int(input('index %d :'%(i)))
    list_1.append(x)

print('your list is ',list_1)
print('negative numbers are')
for i in list_1:
    if i<0:
        print(i )

