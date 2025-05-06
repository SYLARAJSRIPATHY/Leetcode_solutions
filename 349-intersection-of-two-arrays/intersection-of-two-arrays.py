class Solution(object):
    def intersection(self, nums1, nums2):
        intersec = set(nums1) & set(nums2)
        return list(intersec)
sol = Solution()
print(sol.intersection([1,2,2,1],[2,2]))