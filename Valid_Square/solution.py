from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = [p1, p2, p3, p4]
        hashmap = dict()
        
        for i in range(3):
            x1, y1 = p[i][0], p[i][1]
            for j in range(i + 1, 4):
                x2, y2 = p[j][0], p[j][1]
                d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                if d not in hashmap:
                    hashmap[d] = 1
                else:
                    hashmap[d] += 1
        
        x = sorted(list(hashmap.values()))
        return x[0] == 2 and x[1] == 4