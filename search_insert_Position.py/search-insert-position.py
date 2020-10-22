class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i + 1] > target:
                return i + 1