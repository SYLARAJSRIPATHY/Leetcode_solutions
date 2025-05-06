class Solution(object):
    def maximumWealth(self, accounts):
        sums = [sum(row) for row in accounts]
        return max(sums)

sol = Solution()
print(sol.maximumWealth([[1,2,3],[3,2,1]]))