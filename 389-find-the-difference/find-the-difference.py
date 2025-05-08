from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        S = Counter(s)
        T = Counter(t)
        diff = T - S 
        return list(diff.keys())[0]

sol = Solution()
print(sol.findTheDifference("abcd","abcde"))

