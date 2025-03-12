def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    return union, intersection, difference

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union, intersection, difference = set_operations(set1, set2)
print("Union:", union)
print("Intersection:", intersection)
print("Difference (set1 - set2):", difference)
