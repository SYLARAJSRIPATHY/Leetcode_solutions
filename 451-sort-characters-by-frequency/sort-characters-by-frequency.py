from collections import Counter
class Solution:
    def frequencySort(self, s):
        count = Counter(s)
        sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
        result = ''.join([char * freq for char, freq in sorted_chars])
        return result

sol = Solution()
