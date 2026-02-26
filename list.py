
student = {
    "name": "Karthik",
    "age": 20,
    "course": "B.Tech",
    "marks": 85
}
print("Original Dictionary:", student)
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
removed_value = student.pop("marks")
print("\nAfter pop('marks'):", student)
print("Removed value:", removed_value)
del student["age"]
print("\nAfter deleting 'age':", student)