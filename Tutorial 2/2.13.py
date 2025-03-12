"""Write Python script for converting Binary number into decimal number."""


def binary_to_decimal(binary_str):
    return int(binary_str, 2)

binary_str = input("Enter a binary number: ")
print("Decimal representation:", binary_to_decimal(binary_str))
