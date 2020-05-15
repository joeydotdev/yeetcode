"""
Input: [1,1,2,3,3,4,4,8,8]
Output: 2


idx = 4

 1 1 2 2 3 3
         ^
[1,1,2,3,3,4,4,8,8]
         ^

[1,1,2,3,3,4,4,8,8]
     ^
low = 0
hi = 4

mid = 2


[1,1,2,3,3,4,4]
       ^
low = 0
high = 6

mid = 3



check if current element is odd element out
    return True
if my mid idx is even:
    arr[mid_idx+1] should be the same element
    if is same element
        the odd number out is on the right half of array
    else
        the odd number is on the left half of the array

"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        low, high, = 0, len(nums) - 1
        def is_odd_element(idx):
            if idx == 0:
                return nums[idx] != nums[idx+1]
            elif idx == len(nums) - 1:
                return nums[idx] != nums[idx-1]
            else:
                candidate = nums[idx]
                return candidate != nums[idx-1] and candidate != nums[idx+1]
                
        while low <= high:
            mid = (low + high) // 2
            if is_odd_element(mid):
                return nums[mid]
            if mid % 2 == 0:
                # Edge case
                if mid == len(nums) - 1:
                    return -1
                if nums[mid+1] == nums[mid]:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                # midpoint is odd idx
                if mid == len(nums) - 1:
                    return -1
                if nums[mid+1] == nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1