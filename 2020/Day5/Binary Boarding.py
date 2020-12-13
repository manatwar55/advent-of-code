seatIDList = []

def findSeat(maxSeatID):
    seatIDList.sort()
    for i in range(maxSeatID):
        if seatIDList[i] == seatIDList[i-1] +2:
            return(seatIDList[i] -1) 
    return(-1)

def getSeatIDs(data):
    for x in data:
        row = convertRow(x[0:7])
        col = convertCol(x[7:10])
        seatID = row * 8 + col
        seatIDList.append(seatID)


def convertRow(rowBinary):
    rowBinary = rowBinary.replace('F', '0')
    rowBinary = rowBinary.replace('B', '1')
    rowNumber = int(rowBinary, 2)
    return(rowNumber)
        


def convertCol(colBinary):
    colBinary = colBinary.replace('L', '0')
    colBinary = colBinary.replace('R', '1')
    colNumber = int(colBinary, 2)
    return(colNumber)

with open('input.txt', 'rt') as f:
        data = [line.strip() for line in f.readlines()]

getSeatIDs(data)
maxSeatID = max(seatIDList)
mySeat = findSeat(maxSeatID)
print(maxSeatID)
print(mySeat)