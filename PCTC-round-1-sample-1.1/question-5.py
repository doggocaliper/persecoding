first_number = int(input("Enter the first number: "))
while first_number not in range(-100, 101):
    first_number = int(input("Enter the first number: "))
operator = str(input("Enter an operator ( + / *): "))
second_number = int(input("Enter the second number: "))
while second_number not in range(-100, 101):
    second_number = int(input("Enter the second number: "))
if operator == "+":
    print(first_number + second_number)
elif operator == "*":
    print(first_number * second_number)
else:
    print("The operator you entered was invalid.")
