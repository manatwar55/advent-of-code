import collections

contains = collections.defaultdict(list)
containedIn = collections.defaultdict(list)

def initialSplit(x):
    x = x.replace("bags", "")
    x = x.replace("bag", "")
    x = x. replace(".", "")
    bigBag, littleBags = x.split(" contain ")
    bigBag = bigBag.strip()
    return(bigBag, littleBags)

def splitContained(littleBags):
    listOfBags = littleBags.split(", ")
    justTheBags = [y.replace("other", "none") for y in (x.strip() for x in (bag.split(" ", 1)[1] for bag in listOfBags))]
    theNumbers = [z.replace("no", "0") for z in (bag.split()[0] for bag in listOfBags)]
    return(justTheBags, theNumbers)

def createDict(data):
    for x in data:
        i = 0
        bigBag, littleBags = initialSplit(x)
        justTheBags, theNumbers = splitContained(littleBags)
        for bag in justTheBags:
            if bag != "none":
                containedIn.setdefault(bag, []).append(bigBag)
            contains.setdefault(bigBag, []).append(theNumbers[i]+"."+bag)
            i += 1

def findNumContainers(input):
    outer_bags = set()
    for bag in containedIn[input]:
        outer_bags.add(bag)
        outer_bags |= findNumContainers(bag)
    return outer_bags

def findInnerBags(input):
    inner_bags = 0
    for bag in contains[input]:
        count = int(bag.split(".")[0])
        inner_bags += count
        inner_bags += count * findInnerBags(bag.split(".")[1])
    return inner_bags

with open('input.txt', 'rt') as f:
        data = [line.strip() for line in f.readlines()]

createDict(data)
outer_bags = findNumContainers("shiny gold")
inner_bags = findInnerBags("shiny gold")
print(len(outer_bags))
print(inner_bags)