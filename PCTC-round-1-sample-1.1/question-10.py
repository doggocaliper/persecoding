# idk how to count in repeated alphabet

milkshake = ["I", "I", "M", "C", "C", "C", "W"]
blender1 = []
print(milkshake)

blender = str(input("Enter in 6 of the characters in 'milkshake': "))
for i in blender:
    blender1.append(i)

for c in milkshake:
    if c not in blender1:
        print(c)
