
def sum_of_odd_numbers(lower, upper):
    total = 0
    for num in range(lower, upper + 1):
        if num % 2 != 0:
            total += num
    return total

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

total_sum = sum_of_odd_numbers(lower, upper)

print(f"The sum of odd numbers between {lower} and {upper} is: {total_sum}")
