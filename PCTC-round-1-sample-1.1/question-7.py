list1 = []

letter1 = str(input("Enter the first letter: "))
letter2 = str(input("Enter the second letter: "))
letter1.upper()
letter2.upper()

list1.append(letter1)
list1.append(letter2)

list1 = sorted(list1)

newstring = ''.join(list1)

print(newstring)
