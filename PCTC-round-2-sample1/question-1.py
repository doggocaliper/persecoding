x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
z = float(input("Enter the third number: "))

if (x < y) and (y < z):
    print("UP")
elif (x > y) and (y > z):
    print("DOWN")
else:
    print("WOBBLY")
