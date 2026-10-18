def countingZeros():
    with open("day 1/input.txt", "r") as f:
        lines = f.readlines()

    pos = 50

    count = 0

    for line in lines:
        line = line.strip()

        direction = line[0]
        steps = int(line[1:])
        for i in range(steps):
            if direction == 'L':
                pos = (pos - 1) % 100

            elif direction == 'R':
                pos = (pos + 1) % 100

            if pos == 0:
                count += 1
   
    return count

print(countingZeros())