class Solution(object):
    def merge(self, intervals):
        intervals.sort()  # Sort intervals based on starting point
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))