def sum_of_divisors(number):
    divisors_sum = 1  # Start with 1 as 1 is a divisor for all numbers
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:  # Avoid counting the same divisor twice for perfect squares
                divisors_sum += number // i
    return divisors_sum

def find_amicable_numbers(start, end):
    amicable_pairs = []
    for num in range(start, end + 1):
        sum_divisors = sum_of_divisors(num)
        if sum_divisors != num and sum_of_divisors(sum_divisors) == num and (sum_divisors, num) not in amicable_pairs:
            amicable_pairs.append((num, sum_divisors))
    return amicable_pairs

# Example usage:
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

amicable_numbers = find_amicable_numbers(start_range, end_range)
print("Amicable Numbers within the specified range:")
for pair in amicable_numbers:
    print(f"{pair[0]} and {pair[1]} are amicable.")
