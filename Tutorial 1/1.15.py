
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):  
        if number % i == 0:
            return False
    return True

print("Prime numbers less than 1000 are:")
for num in range(2, 1000):
    if is_prime(num):
        print(num, end=" ")
