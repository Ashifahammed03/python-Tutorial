from collections import Counter

def find_mode(numbers):
    count = Counter(numbers)
    max_frequency = max(count.values())
    mode = [num for num, freq in count.items() if freq == max_frequency]
    return mode

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
mode = find_mode(numbers)
print("Mode(s):", mode)
