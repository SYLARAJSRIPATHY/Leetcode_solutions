class Solution(object):
    def isPalindrome(self, s):
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
                
        left, right = 0, len(clean) -1

        while left < right:
            if clean[left] != clean[right]:
                return False

            left += 1
            right -= 1
        return True

sol = Solution()
print(sol.isPalindrome(["A man, a plan, a canal: Panama"]))
print(sol.isPalindrome(["race a car"]))