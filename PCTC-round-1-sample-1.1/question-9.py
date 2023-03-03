first_dance_character = str(input("Enter the first dance character: "))
if first_dance_character == "<":
    print("<+&><+&>")
elif first_dance_character == "+":
    print("+&><+&><")
elif first_dance_character == "$":
    print("&><+&><+")
elif first_dance_character == ">":
    print("><+&><+&")
else:
    print("The character is not part of the dance sequence and is invalid.")
