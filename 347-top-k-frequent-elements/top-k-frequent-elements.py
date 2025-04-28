class Solution(object):
    def topKFrequent(self, nums, k): 
        freq = {}  
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sorted_nums = sorted(freq, key=lambda x: freq[x], reverse=True)

        return sorted_nums[:k]

sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) 
