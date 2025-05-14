class Solution(object):
    def dailyTemperatures(self, temp):
        ans = [0]*len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans
sol = Solution()