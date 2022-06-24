# linear search starts from fist conscuitively 
# iterative
from typing import List
def linear(arr: List[int],target: int):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    return -1
        
print(linear([2,7,13,14,28], 14))


# recursive way
# curr_index=len(arr)-1
def search(arr, curr_index, key):
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)

print(search([2,7,13,14,28,34,45,67,89],8, 34))