print("exercise 1")
import random
sum = 0
rolls = input("Enter number of times to roll: ")
for n in range(0, int(rolls)):
    dice = random.randint(1, 6)
    sum = sum + dice
print("the sum of all rolls: " + str(sum))
