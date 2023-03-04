# Question 1

starfish = int(input("Enter the number of starfish(es): "))
while starfish not in range(0, 101):
    starfish = int(input("Enter the number of starfish(es): "))
spider = int(input("Enter the number of spider(s): "))
while spider not in range(0, 101):
    spider = int(input("Enter the number of spider(s): "))
scorpion = int(input("Enter the number of scorpion(s): "))
while scorpion not in range(0, 101):
    scorpion = int(input("Enter the number of scorpion(s): "))

print((starfish * 5) + (spider * 8) + (scorpion * 12))
