def separate_elements(lst):
    integers = []
    floats = []
    strings = []
    
    for element in lst:
        if isinstance(element, int):
            integers.append(element)
        elif isinstance(element, float):
            floats.append(element)
        elif isinstance(element, str):
            strings.append(element)
    
    return integers, floats, strings

lst = [1, 2.5, "hello", 3, 4.7, "world", 10]
integers, floats, strings = separate_elements(lst)
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
