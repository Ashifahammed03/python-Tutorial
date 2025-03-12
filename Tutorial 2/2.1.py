
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in s if char not in vowels])
    return result

input_string = input("Enter a string: ")

print("String after removing vowels:", remove_vowels(input_string))
