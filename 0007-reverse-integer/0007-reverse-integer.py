class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        
        rev = rev * sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

#-----------------------------------------
        # z = str(x)
        # rev = ""
        # for ch in z:
        #     if ch == 0:
        #         pass
        #     else:
        #         if rev and rev[0] in "-+":
        #             rev = rev[0] + ch + rev[1:]
        #         else:
        #             rev = ch + rev
        # return int(rev)
        