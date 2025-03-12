
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
      for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count

n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_count, odd_count = count_even_odd(numbers)

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
