def sledPolicy(data):
    goodPass = 0

    for x in data:
        splitA = x.split('-', 1)
        minNum = int(splitA[0])
        splitB = splitA[1].split(None, 1)
        maxNum = int(splitB[0])
        splitC = splitB[1].split(':', 1)
        policy = splitC[0]
        polCount = splitC[1].count(policy)
        if minNum <= polCount and polCount <= maxNum:
            goodPass = goodPass + 1
    
    print(goodPass)

def actualPolicy(data):
    goodPass = 0
    for x in data:
        splitA = x.split('-', 1)
        a = int(splitA[0])
        splitB = splitA[1].split(None, 1)
        b = int(splitB[0])
        splitC = splitB[1].split(':', 1)
        policy = splitC[0]
        password = splitC[1].strip()
        length = len(password)
        if a <= length:
            alpha = password[a-1]
        if b <= length:
            beta = password[b-1]
        if alpha != beta and (alpha == policy or beta == policy):
                goodPass = goodPass + 1
        
    print(goodPass)

with open('input.txt', 'rt') as f:
        data = [line.strip() for line in f.readlines()]

sledPolicy(data)
actualPolicy(data)
