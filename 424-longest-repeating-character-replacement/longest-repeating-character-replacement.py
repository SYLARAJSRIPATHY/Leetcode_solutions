class Solution(object):
    def characterReplacement(self, s, k):
        fre = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            fre[char] = fre.get(char, 0) + 1
            max_fre = max(fre.values())

            if (right - left + 1) - max_fre > k:
                fre[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
sol = Solution()
print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 1))