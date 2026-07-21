class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(first):
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    if first:
                        right = mid - 1   # search left
                    else:
                        left = mid + 1    # search right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [binary(True), binary(False)]