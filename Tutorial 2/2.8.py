
def replace_substring(s, old_sub, new_sub):
    return s.replace(old_sub, new_sub)

input_string = input("Enter a string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")

print("Modified string:", replace_substring(input_string, old_substring, new_substring))
