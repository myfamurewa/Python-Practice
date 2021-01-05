from typing import List, Dict
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        my_queue = deque([(amount, 0)])
        already_checked = set([])
        while my_queue:
            amount, level = my_queue.popleft()
            if amount == 0:
                return level
            for coin in coins:
                diff = amount - coin
                if diff >= 0 and diff not in already_checked:
                    already_checked.add(diff)
                    my_queue.append((diff, level + 1))
        return -1