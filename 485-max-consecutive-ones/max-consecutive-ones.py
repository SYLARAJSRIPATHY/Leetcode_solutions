class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count
sol = Solution()
print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))

