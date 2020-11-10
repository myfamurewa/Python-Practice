from typing import List

class Solution:
    
    def maxCoinsRecursive(self, nums: List[int], left_ind: int, right_ind: int) -> int:
        pointer = f"{left_ind}:{right_ind}"
        if pointer in self.cache:
            return self.cache[pointer]
        
        if right_ind < left_ind:
            return 0
        if right_ind == left_ind:
            partial_sum = nums[right_ind]
            if left_ind - 1 >= 0:
                partial_sum *= nums[left_ind - 1]
            if right_ind + 1 <= self.right_upper_bound:
                partial_sum *= nums[left_ind + 1]
            self.caches[pointer] = partial_sum
            return partial_sum

        max_sum = 0
        for i in range(left_ind, right_ind + 1):
            partial_sum = nums[i]
            if left_ind - 1 >= 0:
                partial_sum *= nums[left_ind - 1]
            if right_ind + 1 <= self.right_upper_bound:
                partial_sum *= nums[right_ind + 1]
            coins_from_left_pops = self.maxCoinsRecursive(nums, left_ind, i - 1)
            coins_from_right_pops = self.maxCoinsRecursive(nums, i + 1, right_ind)
            partial_sum = partial_sum + coins_from_left_pops + coins_from_right_pops
            max_sum = max(max_sum, partial_sum)
        self.cache[pointer] = max_sum
        return max_sum

    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            mx = max(nums[0], nums[1])
            mn = min(nums[0], nums[1])
            return (mn * mx) + mx
        self.right_upper_bound = len(nums) - 1
        self.cache = {}

        return self.maxCoinsRecursive(nums, 0, self.right_upper_bound)


# checking