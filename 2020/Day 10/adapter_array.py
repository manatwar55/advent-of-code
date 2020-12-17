import collections

# I'm not proud of the frequency in which I must resort to copying Max
def numRoutes(data):
    routes = collections.defaultdict(lambda : 0)
    routes[0] = 1
    for a in data[1:]:
        routes[a] = sum([routes[a-x] for x in [1,2,3]])
    return max(routes.values())

# There is a clear difference in appearence between Max's code and my own
def findAdaptersDiffs(data):
    data.insert(0, 0)
    diffOf1 = 0
    diffOf2 = 0
    diffOf3 = 0
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if diff == 1:
            diffOf1 += 1
        if diff == 2:
            diffOf2 += 1
        if diff == 3:
            diffOf3 += 1
        lastAdapter = data[i]
    diffOf3 += 1
    return(diffOf1, diffOf2, diffOf3)

with open('input.txt', 'rt') as f:
        data = [int(line.strip()) for line in f.readlines()]

data.sort()
diffOf1, diffOf2, diffOf3 = findAdaptersDiffs(data)
print(diffOf1 * diffOf3)
routes = numRoutes(data)
print(routes)