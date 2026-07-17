class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k =1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1

        # nums[:k]
        return k



#---------------not sorted array-----

        # fin_list = []
        # for i in nums:
        #     if i not in fin_list:
        #         fin_list.append(i)
            
        # for i in range(len(fin_list)):
        #     nums[i] = fin_list[i]
        
        # return len(fin_list)
