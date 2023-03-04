w = str(input("Enter a word: "))
n = int(input("Enter a positive whole number: "))

if len(w) == n:
    print("MATCH")
elif len(w) > n:
    print("MORE")
else:
    print("FEWER")
