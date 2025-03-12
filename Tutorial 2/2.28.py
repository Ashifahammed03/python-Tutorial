def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

lst = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_lst = sort_list(lst)
print("Sorted list:", sorted_lst)
