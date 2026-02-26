lst = [(1, 5), (2, 3), (3, 8), (4, 1)]
print("Original list:", lst)
lst.sort(key=lambda x: x[-1])
print("Sorted list:", lst)
