def collatz(number):
    if (number % 2 == 0):
        return int(number / 2)
    else:
        return int(number * 3 + 1)

try:
    x = int(input("Please input a number to Collatz on: "))
except ValueError:
    print("Please enter an integer")
else:
    while x != 1:
        x = collatz(x)
        print(x)