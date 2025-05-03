class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        missing = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                missing.append(i)
        return missing

sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
