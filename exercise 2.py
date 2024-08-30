
print("exercise 2")
numbers = []
user = input("Enter a list of numbers to be sorted, press enter to stop: ")

while user != '':
    number = float(user)
    numbers.append(number)
    user = input("Enter a list of numbers to be sorted, press enter to stop: ")

numbers.sort(reverse = True)
#print("Sorted numbers:", numbers)
largest = []
largest.extend(numbers[:5])

print("the 5 largest numbers from your list:", str(largest))