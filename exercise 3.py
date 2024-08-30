print("exercise 3")
inp = int(input("enter a number to check: "))
for i in range(2, 10):
    if inp % i == 0 and inp != i:
        print("your number is not a prime number")
        break
else:
    print("your number is a prime number")
