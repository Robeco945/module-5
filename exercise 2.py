print("exercise 2")
num = []
user = input("Enter a list of numbers to be sorted, press enter to stop: ")
while user != '':
    num.append(user)
    user = input("Enter a list of numbers to be sorted, press enter to stop: ")
    num.sort(reverse=True)
print(num)