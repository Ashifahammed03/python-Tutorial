def remove_words_from_string(input_str, words_to_remove):
    words = input_str.split()
    filtered_words = [word for word in words if word not in words_to_remove]
    return ' '.join(filtered_words)

input_str = input("Enter a string: ")
words_to_remove = input("Enter words to remove (separated by space): ").split()

print("String after removal:", remove_words_from_string(input_str, words_to_remove))
