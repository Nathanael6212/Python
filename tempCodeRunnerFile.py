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