from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransome = Counter(ransomNote)
        maga = Counter(magazine)
        for char in ransome:
            if ransome[char] > maga.get(char,0):
                return False
        return True

sol = Solution()
print(sol.canConstruct("aabbc", "aabbbc"))
print(sol.canConstruct("aabbc", "abc"))      
        
