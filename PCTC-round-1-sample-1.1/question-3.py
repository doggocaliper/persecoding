word = str(input("Enter a word: "))
while len(word) not in range(0, 50):
    word = str(input("Enter a word that has less than 50 characters: "))
while word.islower == False:
    word = str(input("Enter a word that only has lower characters of the alphabet: "))

new_word = word * 2
counter = 3

while len(new_word) <= 30:
    new_word = word * int(counter)
    counter = counter + 1

print(new_word)
