def house_Robber(nums):
    sortednums = sorted([(num, i) for num, i in enumerate(nums)], key=lambda x: x[1], reverse=True)
    total = 0
    previous = sortednums[0][0]
    for num in sortednums:
        if num[0] == previous + 1 or previous - 1:
            # print("previous", previous, "continuing")
            continue
        total += num[1]
        previous = num[0]

    return total

print(house_Robber([1,2,3,1]))
def house_RobberV2(nums):
    oddtotal = 0
    eventotal = 0

    for num, i in enumerate(nums):
        if i % 2 == 0:
            eventotal += num
        else:
            oddtotal += num
    return max(eventotal, oddtotal)

print(house_RobberV2([1,2,3,1]))

def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = c = 0
        for i in range(n):
            c = max(a + nums[i], b)
            a, b = b, c
        return c