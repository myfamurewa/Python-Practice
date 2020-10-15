def rotate(nums, k):
    length = len(nums)
    if k == 0 or length == 0:
        return
    rotations = 0
    while rotations < k % length:
        removed = nums.pop()
        nums.insert(0, removed)
        rotations += 1


def rotateV2(nums, k):
    length = len(nums)
    true_rotations = k % length
    for i in range(true_rotations):
        removed = nums.pop()
        nums.insert(0, removed)

def rotateV3(nums, k):
    length = len(nums)
    true_rotations = k % length
    # print("true_rotations", true_rotations)
    # removal_start = length - (k + 1)
    # print("removal start", removal_start)
    rotated = nums[true_rotations+1:]
    rotated = rotated[::-1]
    nums = nums[0:true_rotations+1]
    nums = nums + rotated
    # for num in rotated:
    #     nums.insert(0, num)
t1 = [1,2,3,4,5,6,7]
# print(t1)
# print(rotateV3(t1, 3))
print(t1[:])

def rotateOptimal(nums, k):
    n = len(nums)
    k %= n
    
    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1
            
            if start == current:
                break
        start += 1