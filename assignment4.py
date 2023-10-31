"""
Assignment 4: "Processing Data"

Author: Kirti Subramanian
CWID: 20531478
Date: 10/23/2022

Program Description: This program accepts numbers from the user one at a time. Then, it computes the total,
the largest number, the smallest number, and the count of even and odd numbers. It then prints the results
in the console.
"""

# Get the first number from the user.
number = int(input("Please type a number: "))

# Initialize the total, the largest number, the smallest number, the number count, and the number of even and
# odd numbers.
even_count = 1 if number % 2 == 0 else 0
odd_count = 1 if even_count == 0 else 0
total = number
smallest = number
largest = number
number_count = 1

# Check if the user wants to enter another number or not.
user_choice = input("Do you have another number to enter? ")

# Until the user enters an "N," keep asking the user for a number and recompute all the results.
while user_choice != "N" and user_choice == "Y":
    # Get the number.
    number = int(input("Please type a number: "))
    # Compute the sum.
    total += number
    # Compute the number count (the number of numbers).
    number_count += 1
    # Find the smallest of the numbers.
    if number < smallest:
        smallest = number
    # Find the largest of the numbers.
    if number > largest:
        largest = number
    # Compute the even and odd counts.
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    # Check if the user wants to enter another number or not.
    user_choice = input("Do you have another number to enter? ")

# Calculate the average of all the numbers.
average = "%.1f" % (total / number_count)

# Print the results.
print()
print(f"The total of your numbers is: {total}")
print(f"The smallest of your numbers is: {smallest}")
print(f"The largest of your numbers is: {largest}")
print(f"The number of even numbers is: {even_count}")
print(f"The number of odd numbers is: {odd_count}")
print(f"The average of your numbers is: {average}")

"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment4.py
Please type a number: 7
Do you have another number to enter? Y
Please type a number: -13
Do you have another number to enter? Y
Please type a number: -3
Do you have another number to enter? Y
Please type a number: 99
Do you have another number to enter? N

The total of your numbers is: 90
The smallest of your numbers is: -13
The largest of your numbers is: 99
The number of even numbers is: 0
The number of odd numbers is: 4
The average of your numbers is: 22.5

Process finished with exit code 0
"""