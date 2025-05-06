class Solution(object):
    def sortedSquares(self, nums):
        squares = [x**2 for x in nums]
        return sorted(squares)

sol = Solution()
print(sol.sortedSquares([-4, -1, 0, 3, 10])) 
            
        