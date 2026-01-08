print("factorial of a number without recursion")
x=int(input("enter a number: "))
fact=1
for i in range(x,1,-1):
    fact=fact*i
print("factorial of the given number is: ",fact)
print("factorial of a number with recursion")

def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
print("factorial of",x," is: ",fact(x))
