#  this return the numbers
def sum_two():
    nums = [2,7,11,15]
    target = 9
    for num1 in nums:
        for num2 in nums:
            if num1+ num2==target:
                return num1, num2

print(sum_two())


#  returns the index
def sum_two():
    nums = [2,7,11,15]
    target = 9
    for num1 in nums:
        for num2 in nums:
            if num1+ num2==target:
                return [nums.index(num1) , nums.index(num2)]

print(sum_two())



#  leetcode two sum 
from typing import List
class solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        result = []
        index_map = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i
        return result
ret=solution.twoSum([7,2,13,11,8], 24)
print(ret)


# leetcode in the same way o(n) running time
from typing import List
class Solution:
    def twoSum(numb: List[int], target: int) -> List[int]:
        ind={}
        for i,value in enumerate(numb):
            difference=target-value
            if difference in ind:
                return [i,ind[difference]]
            else:
                ind[value]=i
        
ter=Solution.twoSum([7,2,13,11,8], 24)
print(ter)


# leetcode brute force it with two double for loop o(n^2) running time
from typing import List
class Solution:
    def twoSum(num: List[int],target: int):
        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                if num[i]+num[j]==target:
                    return[i,j]
ter=Solution.twoSum([7,2,13,11,8], 24)
print(ter)







 

