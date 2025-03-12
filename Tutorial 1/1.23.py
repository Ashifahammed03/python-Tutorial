def prime_factors(number):
    factors = []

    while number % 2 == 0:
        factors.append(2)
        number //= 2

    factor = 3
    while factor * factor <= number:
        while number % factor == 0:
            factors.append(factor)
            number //= factor
        factor += 2

    if number > 2:
        factors.append(number)
    
    return factors

num = int(input("Enter a number: "))

factors = prime_factors(num)

print(f"Prime factors of {num} are: {factors}")
