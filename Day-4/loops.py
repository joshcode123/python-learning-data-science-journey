# While loop
num = 1
while num <= 10:
    print("The number is", num)
    num += 1

# For loop with range
for num in range(1, 11):
    if num == 5:
        continue
    elif num == 8:
        break
    print(num)
