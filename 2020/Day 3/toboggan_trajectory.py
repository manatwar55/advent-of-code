def findTreesInSlope(right, down, data):
    skip = 1
    posD = 0
    posR = 0
    count = 0
    for x in data:
        if skip != 1:
            if x[posR % len(x)] == '#':
                count += 1
        posD += 1
        if posD%down == 0:
            skip = 0
            posR += right
        else:
            skip = 1
    return(count)

with open('input.txt', 'rt') as f:
    data = [line.strip() for line in f.readlines()]

oneOne = findTreesInSlope(1, 1, data)
print(oneOne)
threeOne = findTreesInSlope(3, 1, data)
print(threeOne)
fiveOne = findTreesInSlope(5, 1, data)
print(fiveOne)
sevenOne = findTreesInSlope(7, 1, data)
print(sevenOne)
oneTwo = findTreesInSlope(1, 2, data)
print(oneTwo)
finalAnswer = oneOne*threeOne*fiveOne*sevenOne*oneTwo
print(finalAnswer)