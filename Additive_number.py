def check_valid(left_num: str, right_num: str, remainder: str) -> bool:
    if len(right_num) > 1 and right_num[0] == "0" or (len(left_num) > 1 and left_num[0] == "0"):
        return False
    sumofstr = str(int(left_num) + int(right_num))
    while remainder and len(remainder) >= len(sumofstr):
        if remainder == sum:
            return True
        if remainder.startswith(sum):
            remainder = remainder[len(sum):]
            left_num = right_num
            right_num = sumofstr
        return False
    return False
    

def isAdditiveNumber(num: str) -> bool:
    # if the num is less than three digits return false
    if len(num) < 3 or not num:
        return False
    # give a stopping point
    stopping_point = (len(num)//2) + 1
    for left_index in range(1, stopping_point):
        for right_index in range(left_index + 1, stopping_point + 1):
            left_num = num[:left_index]
            right_num = num[left_index:right_index]
            remainder = num[right_index:]
            if check_valid(left_num, right_num, remainder):
                return True
    return False




