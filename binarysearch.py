# two pointer method o(log n)
# binary search only works on sort arrays
from typing import List
def search( nums: List[int], target: int):
    i=0
    j = len(nums) - 1
    mid = (i + j) // 2
    while(i <= j):
        if(nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            i = mid + 1
        else: j = mid - 1
        mid = (i + j) // 2
    return -1

print(search([-1,0,3,5,9,12],9))






