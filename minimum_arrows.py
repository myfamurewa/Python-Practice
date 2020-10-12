def findMinArrowShots(points):
    intersects = {}
    points = sorted(points, key=lambda x: x[0])
    arrows = 0
    for point in points:
        if point[0] in intersects or point[1] in intersects:
            continue
        else:
            for i in range(point[0], point[1]+ 1):
                intersects[i] = i
            arrows += 1
    
    return arrows


test1 = [[10,16],[2,8],[1,6],[7,12]]
x = findMinArrowShots(test1)
print(x)