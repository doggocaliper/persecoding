numberChoice = int(input("Enter a number :"))
while numberChoice not in range(1, 101):
    numberChoice = int(input("Enter a number between 1 and 100 inclusive: "))

if numberChoice > 50:
    print("yes dream big")
else:
    print("on the small side")
