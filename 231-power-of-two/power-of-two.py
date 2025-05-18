class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        return(n&(n-1)) == 0
sol = Solution()
print(sol.isPowerOfTwo(4))
        