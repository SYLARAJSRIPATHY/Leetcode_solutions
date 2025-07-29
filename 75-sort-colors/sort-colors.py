class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        le = 0
        ri = n -1
        i = 0
        while i <= ri:
            if(nums[i] == 0):
                nums[i], nums[le] = nums[le], nums[i]
                le +=1
                i += 1
            elif (nums[i] ==2):
                nums[i], nums[ri] = nums[ri], nums[i]
                ri -= 1 
            else: 
                i += 1
