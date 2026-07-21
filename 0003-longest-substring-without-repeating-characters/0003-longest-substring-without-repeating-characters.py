class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in last and last[s[right]] >= left:
                left = last[s[right]] + 1

            last[s[right]] = right
            ans = max(ans, right - left + 1)

        return ans


    #========================
        window = []
        max_len = 0

        for ch in s:
            while ch in window:
                window.pop(0)

            window.append(ch)
            max_len = max(max_len, len(window))

        return max_len
