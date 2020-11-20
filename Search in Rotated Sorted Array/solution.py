class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 0 or nums is None:
            return -1
        if length == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        left = 0
        right = length -1
        while left < right:
            midpoint = left + (right - left)// 2
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint
        start = left
        left = 0
        right = nums.length-1
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
        
        while left <= right:
            midpoint = left + (right - left) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint + 1
        
        return -1


class SolutionAlt:
    def search(self, nums: List[int], target: int) -> int:
        nums = list(set(nums))
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # nums[left to mid] is sorted 
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # nums[mid to right] is sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1