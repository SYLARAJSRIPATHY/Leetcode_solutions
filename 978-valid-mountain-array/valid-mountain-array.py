class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        end = len(arr)-1
        while i<end and arr[i] < arr[i+1]:
            i +=1
        if i==0 or i == len(arr)-1:
            return  False
        while i < end and arr[i] > arr[i+1]:
            i +=1
        return i == end
        
        