class Solution:
    def defangIPaddr(self, address):
      new_add = address.replace(".", "[.]")
      return new_add
   
      

sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))


