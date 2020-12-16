import re

hexPattern = re.compile(r'\b[0-9a-f]+\b')

def validate(data):
    byr = iyr = eyr = hgt = hcl = ecl = pid = cid = 0
    count = 0
    for x in data:
        if x == "":
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                count += 1
            byr = iyr = eyr = hgt = hcl = ecl = pid = cid = 0
        else:
            tokens = x.split(' ')
            for tok in tokens:
                field, value = tok.split(":")
                if field == "byr" and int(value) >= 1920 and int(value) <= 2002:
                    byr = 1
                if field == "iyr" and int(value) >= 2010 and int(value) <= 2020:
                    iyr = 1
                if field == "eyr" and int(value) >= 2020 and int(value) <= 2030:
                    eyr = 1
                if field == "hgt":
                    if len(value) == 5:
                        if value[0:3].isnumeric() and value[3:5] == "cm":
                            hgt = 1
                    if len(value) == 4:
                        if value[0:2].isnumeric() and value[2:4] == "in":
                            hgt = 1
                if field == "hcl" and value[0] == '#' and len(value) == 7:
                    if re.search(hexPattern, value[1:7]):
                        hcl = 1
                if field == "ecl" and (value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth"):
                    ecl = 1
                if field == "pid" and value.isnumeric() and len(value) == 9:
                    pid = 1
                if field == "cid":
                    cid = 1
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        count += 1
    return(count)


with open('input.txt', 'rt') as f:
        data = [line.strip() for line in f.readlines()]

x = validate(data)
print(x)