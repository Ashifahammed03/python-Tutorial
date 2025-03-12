def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total
for num in range(100, 1000):
    if sum_of_digits(num) % 9 == 0:
        print(num, end=" ")
