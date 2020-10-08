# def search(self, nums: List[int], target: int) -> int:
def search(nums, target):
    start, end = 0
    while start <= end:
        mid = (end + start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return -1


t1 = [-1,0,3,5,9,12]
t2 = [1, 2, 3, 4, 5, 6, 7, 9, 12, 23]

print(search(t1, 9))
print(search(t2, 2))
