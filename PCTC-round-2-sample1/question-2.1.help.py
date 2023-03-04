# Level 2

# Question 1 (idk)

numbers = str(input("Enter 6 positive whole numbers, with a spacing in between each number: "))
number_list = []
sum_of_numbers = []
index_of_13 = 0
index13 = 0

number_list = [int(n) for n in numbers.split()]

for i in number_list:
    index_of_i = number_list.index(i)
    if i == 13:
        index_of_13 = number_list.index(13)
        index13 = int(index_of_13)
    elif index_of_i == (index13 + 1):
        pass
    else:
        sum_of_numbers.append(i)
    index_of_i = 0
    index_of_13 = 0
    index13 = 0

print(sum(sum_of_numbers))
