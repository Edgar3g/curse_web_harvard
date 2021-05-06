import sys

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
    except ValueError:
        print("Error: Dont's a number")
        sys.exit(1)

    try:
        result = x // y
    except ZeroDivisionError:
        print("Error: Cannot divide by 0.")
        sys.exit(1)

    print(f" {x} / {y} = {result}")

 