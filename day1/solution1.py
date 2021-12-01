increasedHeightCounter = 0
previous = 0
with open('input.txt') as input:
    for current in input:
        if previous != 0 and int(current) > int(previous):
            increasedHeightCounter += 1
        previous = current
print(increasedHeightCounter)