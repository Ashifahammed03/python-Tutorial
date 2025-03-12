
def calculate_sum_and_average(numbers):
    positive_sum = 0
    negative_sum = 0
    positive_count = 0
    negative_count = 0
    
    for num in numbers:
        if num > 0:
            positive_sum += num
            positive_count += 1
        elif num < 0:
            negative_sum += num
            negative_count += 1
  
    if positive_count > 0:
        positive_average = positive_sum / positive_count
    else:
        positive_average = 0
    
    if negative_count > 0:
        negative_average = negative_sum / negative_count
    else:
        negative_average = 0
    
    return positive_sum, positive_average, negative_sum, negative_average

numbers = []
for i in range(4):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

positive_sum, positive_average, negative_sum, negative_average = calculate_sum_and_average(numbers)

print(f"Sum of positive numbers: {positive_sum}")
print(f"Average of positive numbers: {positive_average:.2f}")
print(f"Sum of negative numbers: {negative_sum}")
print(f"Average of negative numbers: {negative_average:.2f}")
