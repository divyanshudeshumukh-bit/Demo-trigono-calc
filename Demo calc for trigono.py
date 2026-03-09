import math

while True:

    angle = float(input("Enter angle: "))
    choice = input("Choose sin / cos / tan: ")

    radian = math.radians(angle)

    if choice == "sin":
        result = math.sin(radian)

    elif choice == "cos":
        result = math.cos(radian)

    elif choice == "tan":
        result = math.tan(radian)

    else:
        print("Invalid choice")
        continue

    print("Result:", result)

    again = input("continue (yes/no): ")

    if again == "no":
        print("Calculator stopped")
        break
