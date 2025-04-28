class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)

        return list(anagram_map.values())

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        