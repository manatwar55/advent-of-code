# Check to see if adjacent spots are occupied.
def check_near(i, j, data, empty):
    count = 0
    # Avoid out of bounds and the central seat
    # while checking nearby seats.
    for x in range(-1, 2):
        if i+x <= -1 or i+x >= len(data):
            continue
        for y in range(-1, 2):
            if (j+y <= -1 or j+y >= len(data[i+x]) or \
                 (x == 0 and y == 0)):
                continue
            # Count each time we have a nearby seat occupied.
            if data[i+x][j+y] == '#':
                count += 1
                # This seat shouldn't be occupied.
                if empty or count >= 4:
                    return False
    return True

# Check to see if within line of sight seats are occupied.
def check_sight(i, j, data, empty):
    count = 0

# Look for occupied and empty seats.
def scan_seats(data):
    occupied = 0

    # Monitor if any changes occur at each pass.
    change = True
    while change:
        data_copy = [row[:] for row in data]
        change = False
        for i in range(len(data_copy)):
            for j in range(len(data_copy[i])):
                # Current position is an occupied seat
                if data_copy[i][j] == '#':
                    if check_near(i, j, data, False) == False:
                        data_copy[i][j] = 'L'
                        occupied -= 1
                        change = True
                # Current position is an empty seat
                elif data_copy[i][j] == 'L':
                    if check_near(i, j, data, True) == True:
                        data_copy[i][j] = '#'
                        occupied += 1
                        change = True
        # Update data for next pass
        data = [row[:] for row in data_copy]
    return occupied

with open('input.txt', 'rt') as f:
        data = [list(line.strip()) for line in f.readlines()]

# Call the code for part 1
occupied = scan_seats(data)
print(occupied)