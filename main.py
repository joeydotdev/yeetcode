from collections import defaultdict

def max_sub_array_of_size_k(arr, k):
    max_sum = float('-inf')
    if k <= 0:
        return max_sum

    l = 0 
    cur = 0
    for r in range(len(arr)):
        cur += arr[r]

        if r - l >= k - 1:
            max_sum = max(max_sum, cur)
            cur -= arr[l]
            l += 1

    return max_sum

def smallest_subarray_with_given_sum(arr, s):
    l = 0
    smallest_window = float('inf')
    cur_sum = 0
    for r in range(len(arr)):
        cur_sum += arr[r]

        while cur_sum >= s and l <= r:
            smallest_window = min(smallest_window, r - l + 1)
            cur_sum -= arr[l]
            l += 1
    
    return smallest_window if smallest_window < float('inf') else -1

def fruits_into_baskets(fruits):

    lookup = {}
    l = 0
    longest = float('-inf')
    for r, ch in enumerate(fruits):
        if ch not in lookup:
            lookup[ch] = 1
        else:
            lookup[ch] += 1
        while len(lookup) > 2 and l <= r:
            lookup[fruits[l]] -= 1
            if lookup[fruits[l]] == 0:
                del lookup[fruits[l]]
            l += 1
        longest = max(longest,r-l+1)

    longest = max(longest, r-l+1)
        
    return longest if longest > float('-inf') else -1

def non_repeat_substring(s):
    if s is None or len(s) == 0:
        return 0
    
    lookup = {}
    l = 0
    global_max = float('-infinity')

    for r, ch in enumerate(s):
        if ch in lookup:
            l = max(l, lookup[ch] + 1)
        
        lookup[ch] = r
        global_max = max(global_max, r - l + 1)

    return global_max

def length_longest(s, k):
    lookup = [0] * 26
    l = 0
    max_char = 0
    max_count = 0

    for r, ch in enumerate(s):
        idx = ord(ch) - ord('a')
        lookup[idx] += 1
        max_char = max(max_char, lookup[idx])

        while r - l + 1 - max_char > k:
            lookup[ord(s[l]) - ord('a')] -= 1
            l += 1
        
        max_count = max(max_count, r - l + 1)

    return max_count

# 3 - 0 + 1 - 3

# 4 - 1 + 1 - 2 > 1

print(length_longest("aabccbb", 2)) 

# print(non_repeat_substring("foo")) # 2
# print(non_repeat_substring("abcd")) # 4
# print(non_repeat_substring("corgi")) # 5
# print(non_repeat_substring("dog")) # 3
# print(non_repeat_substring("aabccbb")) # 3
# print(non_repeat_substring("abbbb")) # 2
# print(non_repeat_substring("abccde")) # 3
# print(non_repeat_substring("")) # 0
# print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
# print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
# print(longest_substring_with_k_distinct('fooobar', 2))
# print(longest_substring_with_k_distinct('araaci', 2))
# print(longest_substring_with_k_distinct('araaci', 1))
# print(longest_substring_with_k_distinct('cbbebi', 3))
# print(smallest_subarray_with_given_sum([1,2,3,4], 1))
# print(smallest_subarray_with_given_sum([1,2,3,4], 5))
# print(smallest_subarray_with_given_sum([1,2,3,4], 3))
# print(smallest_subarray_with_given_sum([1,2,3,4], 100000))
# print(max_sub_array_of_size_k([1,2,3,4,5], 1))
# print(max_sub_array_of_size_k([1,2,3,4,5], 3))
# print(max_sub_array_of_size_k([1,2,3,4,5], 2))
# print(max_sub_array_of_size_k([-1,1000,3,4,5], 2))