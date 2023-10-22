def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

# Example usage:
input_number = int(input("Enter a number: "))

if is_armstrong(input_number):
    print(f"{input_number} is an Armstrong number!")
else:
    print(f"{input_number} is not an Armstrong number.")

# ToDo: give a bumber, find the next Armstrong number