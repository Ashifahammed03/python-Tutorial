
def remove_substring(s, sub):
    return s.replace(sub, '')

input_string = input("Enter a string: ")
substring = input("Enter the substring to remove: ")

print("Modified string:", remove_substring(input_string, substring))
