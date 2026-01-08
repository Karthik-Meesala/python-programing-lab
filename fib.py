print("fibonacci without recurssion: ")
x=int(input("enter a number : "))
first=0
second=1
print(first,second,end=" ")
for i in range(2,x):
        next=first+second
        print(next,end=" ")
        first=second
        second=next
print("")
print("fibonacci with recurssion: ")
def fib(x):
        if x==0:
                return 0
        elif x==1:
                return 1
        else:
                return fib(x-1)+fib(x-2)

for i in range(0,x):
        print(fib(i),end=" ")