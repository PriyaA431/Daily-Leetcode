class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lst = []
        for num in nums:
            for i in str(num):
                lst.append(int(i)) 

        return lst