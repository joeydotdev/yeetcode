class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        new_list = [x for x in A]
        for i in range(len(new_list)):
            new_list.append(new_list[i])
            
        low = 0
        cur_max = -1000000
        global_max = -1000000

        for i 
        return 1