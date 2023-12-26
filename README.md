# Processing Data

## Overview
This Python program is designed to accept numbers from the user, compute various statistics (like total, largest, smallest number, and count of even and odd numbers), and then display these results.

### Author
- **Author:** Kirti Subramanian
- **CWID:** 20531478
- **Date:** 10/23/2022

## Description
The program prompts the user to enter numbers one at a time. After each number, the user is asked whether they want to enter another number. The program then calculates the total, largest number, smallest number, count of even numbers, count of odd numbers, and the average. These results are printed in the console at the end.

## Features
- **User Input:** Accepts numbers from the user.
- **Calculation:** Computes total, largest, smallest, even count, odd count, and average.
- **Results Display:** Prints the calculated results to the console.

## Usage
### Running the Program
The program starts by asking the user to input a number. After entering each number, the user is prompted to enter another number or end the input process.

### Example Interaction
```python
# Initial Input
Please type a number: 7

# Asking for More Input
Do you have another number to enter? Y

# Further Inputs and Final Output
Please type a number: -13
Do you have another number to enter? Y
Please type a number: -3
Do you have another number to enter? Y
Please type a number: 99
Do you have another number to enter? N

# Output
The total of your numbers is: 90
The smallest of your numbers is: -13
The largest of your numbers is: 99
The number of even numbers is: 0
The number of odd numbers is: 4
The average of your numbers is: 22.5

# Process finished with exit code 0
