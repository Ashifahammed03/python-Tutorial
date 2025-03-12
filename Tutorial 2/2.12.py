def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

decimal_num = int(input("Enter a decimal number: "))
print("Binary representation:", decimal_to_binary(decimal_num))
