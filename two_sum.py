"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx, element in enumerate(nums):
            if element not in lookup:
                lookup[element] = set([]) 

            lookup[element].add(idx)
            desired_num = target - element
            if desired_num not in lookup:
                continue
            if idx in lookup[desired_num] and len(lookup[desired_num]) == 1:
                continue

            for i in lookup[desired_num]:
                if i == idx:
                    continue 
                return [idx, lookup[desired_num]]

        return [-1, -1]