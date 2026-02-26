lst = []
n = int(input("Enter how many numbers: "))
for i in range(1, n + 1):
    lst.append((i, i * i))
print("List of tuples:", lst)
