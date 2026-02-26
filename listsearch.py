student = {
    "101": "Karthik",
    "102": "Ravi",
    "103": "Sai",
    "104": "Surya"
}
print("Dictionary is:", student)
value = input("\nEnter the value to search: ")
found = False
for key in student:
    if student[key] == value:
        print("The key for value", value, "is:", key)
        found = True
        break
if not found:
    print("Value not found in dictionary")