class Solution(object):
    def digit_sum(self, num):
        total = 0
        for digit in str(num):
            total += int(digit)
        return total

    def countLargestGroup(self, n):
        group_counts = {}

        for i in range(1, n+1):
            dsum = self.digit_sum(i)

            if dsum in group_counts:
                group_counts[dsum] += 1
            else:
                group_counts[dsum] = 1

        max_size = max(group_counts.values())
        count = 0
        for val in group_counts.values():
            if val == max_size:
                count += 1

        return count
sol = Solution()
print(sol.countLargestGroup(13))
print(sol.countLargestGroup(2))
