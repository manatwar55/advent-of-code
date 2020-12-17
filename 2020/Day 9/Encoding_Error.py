# Code from Day 1 question
# given a list of data, finds 2 numbers that sum to the value given.
def two_sum(sum, data):    
    myDict = {}
    for x in data:
        find = sum - x
        if find in myDict:
            return(x, find)
        myDict[x] = 1
    return(-1, -1)

# find the number that isn't the sum of 2 numbers within the given preamble.
def findException(data, size=25):
    for i in range(size, len(data)):
        x, y = two_sum(data[i], data[i-size: i])
        if x == -1 or y == -1:
            return(data[i])
    return(-1)

# found this online. Maybe could have found out how to code it myself,
# but not worth the time and effort I saved.
# I understand how it works though. It loops through every subarray
# until we find the subarray we are looking for.
def subArraySum(data, exc):
    for i in range(len(data)):
        curr_sum = data[i]

        j = i + 1
        while j <= len(data):
            
            if curr_sum == exc:
                return(i, j-1)
            if curr_sum > exc or j == len(data):
                break

            curr_sum = curr_sum + data[j]
            j += 1
    return(-1, -1)

# After finding the exception and the subarray that sums to the exception
# find the max and min of that subarray and return the sum of those 2 numbers.
def findWeakness(data, size=25):
    exc = findException(data, size)
    x, y = subArraySum(data, exc)
    large = max(data[x: y+1])
    small = min(data[x: y+1])
    return(large + small)

with open('input.txt', 'rt') as f:
        data = [int(line.strip()) for line in f.readlines()]

result1 = findException(data)
result2 = findWeakness(data)
print(result1)
print(result2)