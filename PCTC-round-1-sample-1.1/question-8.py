day = int(input("Enter a positive whole number: "))

while day not in range(1, 101):
    day = int(input("Enter a positive whole number between 1 and 100 inclusive: "))

print("\./")
for i in range(day):
    print(".|.")
