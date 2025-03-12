def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def separate_prime_composite(lst):
    primes = []
    composites = []
    
    for num in lst:
        if is_prime(num):
            primes.append(num)
        else:
            composites.append(num)
    
    return primes, composites

lst = list(map(int, input("Enter positive integers separated by space: ").split()))
primes, composites = separate_prime_composite(lst)
print("Prime numbers:", primes)
print("Composite numbers:", composites)
