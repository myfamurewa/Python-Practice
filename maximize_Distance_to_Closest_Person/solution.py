from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        spaceBetween = 0
        value = 1
        for seatValue in seats:
            if seatValue == 0:
                value += 1
            elif seatValue == 1:
                if spaceBetween < value:
                    spaceBetween = value
                    value = 1
        if spaceBetween < value:
            spaceBetween += value
        print("spacebetween", spaceBetween)
        if spaceBetween == len(seats) - 1:
            return spaceBetween
        else:
            if spaceBetween % 2 == 1:
                return int(spaceBetween//2)
            elif spaceBetween % 2 == 0:
                return int(spaceBetween/2)


    def maxDistToClosest(self, seats: List[int]) -> int:
    
        prev, max_len = 0, 0
        
        for cur, seat in enumerate(seats):
            if seat:
                if seats[prev]:
                    max_len = max(max_len, (cur - prev) // 2)
                else:
                    max_len = max(max_len, (cur - prev))
                prev = cur
                
        if seats[prev]: 
            max_len = max(max_len, len(seats) - 1 - prev) 
                
        return max_len
        
caller = Solution()
print(caller.maxDistToClosest([1,0,1]))