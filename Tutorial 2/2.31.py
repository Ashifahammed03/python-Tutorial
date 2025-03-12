def remove_all_duplicates(lst):
    unique_elements = []
    for item in lst:
        if lst.count(item) == 1:
            unique_elements.append(item)
    return unique_elements

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("List after removing all duplicates:", remove_all_duplicates(lst))
