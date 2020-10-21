
def asteroidCollision(asteroids):
    rightbound = []
    i = 0
    while(i < len(asteroids)):
        if(asteroids[i]):
            rightbound.append(asteroids[i])
        else:
            while len(rightbound) > 0 and rightbound[-1] > 0 and rightbound[-1] < asteroids[i]:
                rightbound.pop()
        if len(rightbound) == 0 or rightbound[-1] < 0:
            rightbound.append(asteroids[i])
        elif rightbound[-1] == abs(asteroids[i]):
            rightbound.pop()
    return rightbound[::-1]


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            stack.append(ast)
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                if stack[-1] + stack[-2] < 0: stack.pop(-2)
                elif stack[-1] + stack[-2] > 0: stack.pop()
                else:
                    stack.pop(); stack.pop()
                    break
        
        return stack



    



# print(asteroidCollision([5, 10, -5]))
# print(asteroidCollision([8, -8]))
print(asteroidCollision([-2, -1, 1, 2]))
# print(asteroidCollision([10, 2, -5]))

