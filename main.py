

# def main():
#     print("Hello")

# if __name__ == "__main__":
#     main()

# # try/except

# # x = int(input("Please enter a number: "))

# # print(f"The number you chose was {x}")  value error when string is used

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Enter a number: ")


# print(f"The number you chose was {x}")


# menu_items = [
#     "apples",
#     "oranges",
#     "pears",
#     "blueberries"
# ]

# i = 0

# while i < len(menu_items):
#     print(f" {[i + 1]} {menu_items[i]} ")

#     i += 1

# # choice = int(input("Enter a choice: "))

# # item_choice = menu_items[choice - 1] # value error is possible


# while True:
#     try:
#         choice = int(input("Enter a choice: "))
#         item_choice = menu_items[choice - 1]

#         if choice <0:
#             raise ValueError

#         break
#     except (ValueError, IndexError):
#         print("Invalid Input, please select an appropriate number!")

#     # except ValueError:
#     #     print("Please input a number! ")
#     # except IndexError:
#     #     print("Must be from menu (#1-4)!")

# print(f"You chose {item_choice}")








        
# Question 81
# Write a function that takes the lengths of the two shorter sides of a right triangle asits parameters. Return the hypotenuse of the triangle, computed using Pythagoreantheorem, as the function’s result. Include a main program that reads the lengths ofthe shorter sides of a right triangle from the user, uses your function to compute thelength of the hypotenuse, and displays the result.

import math

def main():
    a = float(input("Enter length of side of triangle: "))
    b = float(input("Enter length of side of triangle again: "))

    result = hypo(a, b)
    print(f"The hypotoneuse is {result}")


def hypo(a: float, b:float) -> float:
    return math.sqrt(a**2 + b**2)

while True:
    try:
        a = float(input("Enter length of side of triangle: "))

        if a < 0 :
            raise ValueError
        break
    except ValueError:
        print("Please Enter a number! ")

while True:
    try:
        b = float(input("Enter length of side of triangle again: "))

        if b < 0 :
            raise ValueError
        break
    except ValueError:
        print("Please Enter a number! ")

result = hypo(3, 4)
print(result)

if __name__ == "__main__":
    main()

# Question 82
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25for every 140 meters traveled. Write a function that takes the distance traveled (in kilometers) as its only parameter and returns the total fare as its only result. Write a main program that demonstrates the function.

def main():
    km = float(input("Enter the amount of km travelled: "))

    result = taxi_fare(km)
    print(result)

def taxi_fare(km: float) -> float:
    base_fare = 4
    return round(base_fare + (km * 1000) * (0.25/140), 2)

while True:
    try:
        km = float(input("Enter the amount of km travelled: "))

        if km < 0 :
            raise ValueError
        break
    except ValueError:
        print("Please Enter a number! ")

if __name__ == "__main__":
    main()

#  Question 83
# An online retailer provides express shipping for many of its items at a rate of $10.95 for the first item, and $2.95 for each subsequent item. Write a function that takes the number of items in the order as its only parameter. Return the shipping charge for the order as the function’s result. Include a main program that reads the number of items purchased from the user and displays the shipping charge.

def main():
    item = int(input("How many packages do you want to ship: "))
    result = shipping(item)
    print(result)

def shipping(item: int) -> float:
    if item == 1:
        return 10.95
    else:
        return round(10.95 + 2.95 * (item -1), 2)

while True:
    try:
        item = int(input("How many packages do you want to ship: "))

        if item < 0 :
            raise ValueError
        break
    except ValueError:
        print("Please Enter a number! ")

if __name__ == "__main__":
    main() 

# Question 84
# Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median.

def main():
    num_1 = float(input("Enter a number: "))
    num_2 = float(input("Enter another number: "))
    num_3 = float(input("Enter final number: "))
    result = nmb_3(num_1, num_2, num_3)
    print(result)

def nmb_3(num_1: float, num_2: float, num_3: float) -> float:
    if num_1 < num_2 < num_3 or num_3 < num_2 < num_1 :
        return num_2
    elif num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
        return num_1
    elif num_1 < num_3 < num_2 or num_2 < num_3 < num_1:
        return num_3
    elif num_1 == num_2 or num_1 == num_3 : #if they're are 2 equal numbers
        return num_1
    elif num_3 == num_2: #if they're are 2 equal numbers
        return num_3
    else: #if all numbers are equal
        return num_1 

while True:
    try:
        num_1 = float(input("Enter final number: "))
        break
    except ValueError:
        print("Please Enter a number! ")

while True:
    try:
        num_2 = float(input("Enter final number: "))
        break
    except ValueError:
        print("Please Enter a number! ")

while True:
    try:
        num_3 = float(input("Enter final number: "))
        break
    except ValueError:
        print("Please Enter a number! ")

if __name__ == "__main__":
    main() 


# # Question 85 
# # Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function that takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as its only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty string if a value outside of this range is provided as a parameter. Include a main program that demonstrates your function by displaying each integer from 1 to 12 and its ordinal number. Your main program should only run when your file has not been imported into another program.

def main():
    nmb = int(input("Enter a number: "))
    result = ordinal(nmb)
    print(result)


def ordinal(nmb: int) -> str:
    if nmb == 1:
        return "First"
    elif nmb == 2:
        return "Second"
    elif nmb == 3:
        return "Third"
    else: 
        return ""

while True:
    try:
        nmb = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please Enter a number! ")

if __name__ == "__main__":
    main() 


