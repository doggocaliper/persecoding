# Question 2

letters = str(input("Enter 5 lowercase letters separated by 5 spaces: "))
letters = letters.replace(" ", "")
alphabets = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
             "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letter_list = []
number_list = []

for i in letters:
    letter_list.append(i)

for i in letter_list:
    if i in alphabets:
        number_list.append(alphabets.index(i))
    else:
        break

print(max(number_list) - min(number_list))
