def slice_string(s):
    odd_chars = s[1::2]
    even_chars = s[0::2]
    return even_chars, odd_chars

input_string = input("Enter a string: ")

even_chars, odd_chars = slice_string(input_string)
print("Even index characters:", even_chars)
print("Odd index characters:", odd_chars)
