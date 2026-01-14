class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        count = 0
        prev = 0 
        
        for ch in s:
            curr = values[ch]

            if curr > prev:
                count += curr - 2 * prev
            else:
                count += curr

            prev = curr  
        
        return count
