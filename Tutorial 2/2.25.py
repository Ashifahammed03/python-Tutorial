def remove_duplicates(lst):
    return list(set(lst))

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("List after removing duplicates:", remove_duplicates(lst))
