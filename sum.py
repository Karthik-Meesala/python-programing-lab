lst=[]
n=int(input("enter how many elements: "))
for i in range(n):
    c=int(input("enter a number: "))
    lst.append(c)
print("list elements are: ",lst)
print("sum of the eleents in the list are: ",sum(lst))