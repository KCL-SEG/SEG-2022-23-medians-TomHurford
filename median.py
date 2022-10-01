""" Request a list of comma separated numbers from the user and return the median. """

# Import modules
import sys

# Function to find the median of a list of numbers
def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        return numbers[len(numbers) // 2]

# Main
if __name__ == "__main__":
    # Get user input
    numbers = input("Enter a comma separated list of numbers: ")
    # Convert user input to list of integers
    numbers = [int(n) for n in numbers.split(",")]
    # Print median
    print("The median is: {}".format(median(numbers)))

# End of script