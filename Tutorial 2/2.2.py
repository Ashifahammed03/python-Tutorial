def remove_odd_indices(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 0])

input_string = input("Enter a string: ")

print("String after removing odd index characters:", remove_odd_indices(input_string))
