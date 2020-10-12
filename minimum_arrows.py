def findMinArrowShots(points):
    points = sorted(points, key=lambda x: x[1])
    n, arrows = len(points), 1
    current = points[0]

    for i in range(n):
        if current[1] < points[i][0]:
                arrows += 1
                current = points[i]
    
    return arrows




test1 = [[10,16],[2,8],[1,6],[7,12]]
x = findMinArrowShots(test1)
print(x)

def findMinArrowShotsV1(self, points: List[List[int]]) -> int:
    if len(points) == 1:
        return 1
    intersects = {}
    points = sorted(points, key=lambda x: x[1])
    arrows = 0
    for point in points:
        if point[0] in intersects or point[1] in intersects:
            continue
        else:
            for i in range(point[0], point[1]+ 1):
                intersects[i] = i
            arrows += 1

    return arrows