class Solution(object):
    def moveZeroes(self, nums):
        not_zero = 0

        for i in range(len(nums)):
            if nums[i] !=0:
                nums[not_zero], nums[i] = nums[i], nums[not_zero]
                not_zero +=1
        return
sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))