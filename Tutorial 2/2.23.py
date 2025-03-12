def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Median:", find_median(numbers))
