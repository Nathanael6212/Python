# two pointer method from 1-indexed array of integers
class Solution:
    def sorted_sum(number,target):
            i = 0
            j = len(number) - 1
            while(i < j):
                if (number[i] +number[j] ==target):
                    return [i+1,j+1]
                
                elif(number[i] +number[j]<target):
                    i += 1
                else:
                    j -= 1
            return 0

tr=Solution.sorted_sum([2,7,11,15], 9)
print(tr)

# dictonaries 1-indexed array of integers
from typing import List
class Solution:
    def twoSum(numb: List[int], target: int) -> List[int]:
        ind={}
        for i,value in enumerate(numb):
            difference=target-value
            if difference in ind:
                return [i+1,ind[difference]+1]
            else:
                ind[value]=i
        
ter=Solution.twoSum([2,7,13,11,28], 24)
print(ter)