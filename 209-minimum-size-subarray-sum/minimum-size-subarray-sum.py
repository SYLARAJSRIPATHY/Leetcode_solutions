class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])) 
print(sol.minSubArrayLen(4, [1,4,4])) 
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) 