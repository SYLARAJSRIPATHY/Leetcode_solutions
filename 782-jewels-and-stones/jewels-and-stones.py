class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        return sum(stone in jewel_set for stone in stones)
    
sol = Solution()