
with open ("day 2/input.txt", "r") as f:
    id = f.readline()
    singleID = id.split(",")

sum = 0

for i in singleID:
        start = i.split("-")[0]
        end = i.split("-")[1]
        diff = int(end) - int(start)

        for j in range(int(start), int(end)+1):
            num = str(j)
            mid = len(num) // 2
            left = num[:mid]
            right = num[mid:]

            if left == right:
                sum = sum + int(num)

print(sum)