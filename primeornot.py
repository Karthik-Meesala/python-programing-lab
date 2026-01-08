def prime_without_recursion(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def prime_with_recursion(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return prime_with_recursion(n, i + 1)
num = int(input("Enter a number: "))
if prime_without_recursion(num):
    print("Without Recursion: Prime Number")
else:
    print("Without Recursion: Not a Prime Number")

if prime_with_recursion(num):
    print("With Recursion: Prime Number")
else:
    print("With Recursion: Not a Prime Number")
