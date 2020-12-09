def two_sum(sum, data):    
    myDict = {}
    for x in data:
        find = sum - x
        if find in myDict:
            return(x, find)
        myDict[x] = 1
    return(-1, -1)

def three_sum(sum, data):
    for x in data:
        a, b = two_sum(sum - x, data)
        if a != -1:
            return(x, a, b)
    return(-1, -1, -1)

with open('input.txt', 'rt') as f:
        data = [int(line.strip()) for line in f.readlines()]
x, y = two_sum(2020, data)
a, b, c = three_sum(2020, data)

print(x*y)
print(a*b*c)
