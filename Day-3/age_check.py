# If-else conditions based on age
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
elif age >= 13 and age < 17:
    print("You are a teenager")
else:
    print("You are a child")
