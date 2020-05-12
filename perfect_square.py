"""
	perfect square:
		target = a * a



	16 <=



	low = 1
	hi = num/2 => 8

	16 / 8 = 2
	16 / 4 = 4	



	25 / 12 = 2
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    	low = 1
    	high = num // 2

    	if num <= 1:
    		return True

    	while low <= high:
    		mid = (low + high) // 2
    		cur_val = mid * mid
    		if cur_val == num:
    			return True
    		elif cur_val > num:
    			high = mid - 1
    		else:
    			low = mid + 1

    	return False

