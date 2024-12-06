from collections import defaultdict
def find_duplicates(nums):
    my_dict = defaultdict(int)
    duplicates = []
    for i in nums:
        my_dict[i] += 1
    for key in my_dict:
        if my_dict[key] > 1:
            duplicates.append(key)
    return duplicates

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )
