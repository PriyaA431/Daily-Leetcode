class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev = ""
        for ch in s:
            rev = ch + rev
        if s == rev:
            return True
        else:
            return False

#   ---------------------------------
    #using Slicing
        # if s == s[::-1]:
        #     return True
        # else: 
        #     return False



  

        