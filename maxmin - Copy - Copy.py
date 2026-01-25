lst=[]
n=int(input("enter how many elements: "))
for i in range(n):
    c=int(input("enter a number: "))
    lst.append(c)
print("list elemnts are: ",lst)
print("maximum element is: ",max(lst))
print("minimum element is: ",min(lst))
