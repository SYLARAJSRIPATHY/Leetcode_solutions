class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         maxi = nums[0]
         count = 1
         n = len(nums)
         for i in range(1,n):
            if (nums[i] == maxi):
                count +=1
            else:
                count -=1
                if (count == 0):
                    maxi = nums[i]
                    count = 1
         return maxi