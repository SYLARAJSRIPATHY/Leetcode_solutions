class Solution(object):
    def missingNumber(self, nums):
        n =len(nums)
        total = n*(n+1)//2
        return total - sum(nums)
sol = Solution()
print(sol.missingNumber([0,1]))

        