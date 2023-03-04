list_of_numbers = ["0"]
n = float(input("Enter a positive number: "))
number = 2
answer = 0
power = 1

while int(list_of_numbers[-1]) < n:
    answer = number ** power
    list_of_numbers.append(answer)
    power = power + 1
    answer = 0

print(list_of_numbers[-1])
