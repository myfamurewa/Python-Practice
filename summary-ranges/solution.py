class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return []
        startval = nums[0]
        endval = startval
        result = []
        for i in range(len(nums)):
            try:
                if nums[i + 1] == nums[i] + 1:
                    endval = nums[i+1]
                else:
                    if startval == endval:
                        result.append(str(startval))
                    else:
                        result.append(f"{startval}->{endval}")
                    startval = nums[i + 1]
                    endval = nums[i + 1]
            except:
                if startval == nums[i]:
                    result.append(f"{nums[i]}")
                else:
                    result.append(f"{startval}->{nums[i]}")
                
        return result      
