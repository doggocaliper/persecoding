x = str(input("Enter a word: "))
while len(x) > 100:
    x = str(input("Enter a word that has maximum 100 characters: "))

y = int(input("Enter a number: "))
while y > 100:
    y = int(input("Enter a number that is less than or equals to 100: "))

x = x[::-1]

print(x * y)
