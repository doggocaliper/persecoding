first_number = int(input("Enter the first number = "))
while first_number not in range(0, 1001):
    first_number = int(input("Enter the first number again = "))
second_number = int(input("Enter the second number = "))
while second_number == first_number:
    second_number = int(input("Enter the second number (must be different from first number) = "))
while second_number not in range(0, 1001):
    second_number = int(input("Enter the second number again = "))
if first_number > second_number:
    print(first_number - second_number)
else:
    print(second_number - first_number)
