class NumArray:

    def __init__(self, nums: List[int]):
        self.total = [0]
        running = 0
        for x in nums:
            running += x
            self.total.append(running)

    def sumRange(self, left: int, right: int) -> int:
        return self.total[right +1] - self.total[left]

