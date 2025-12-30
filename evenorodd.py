n=int(input("enter a number: "))
count=0
count1=0
for i in range(n):
    if i%2==0:
        count+=1
    else:
        count1+=1
print("number of even numbers in between ",n," is: ",count)
print("number of odd numbers in between ",n," is: ",count1)
