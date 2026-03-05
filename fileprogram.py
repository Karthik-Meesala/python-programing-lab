import random

file = open("random_numbers.txt", "w")

for i in range(20):
    num = random.randint(1, 100)
    file.write(str(num) + "\n")

file.close()

print("20 random numbers generated and written to file")