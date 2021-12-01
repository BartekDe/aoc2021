increasedHeightCounter = 0
previous = 0
secondPrevious = 0
previousSum = 0
sum = 0
with open('input.txt') as input:
    for current in input:
        if previous != 0 and secondPrevious != 0:
            sum = (int(secondPrevious) + int(previous)) + int(current)
        if previousSum != 0 and sum > previousSum:
            increasedHeightCounter += 1
        secondPrevious = previous
        previous = current
        previousSum = sum
print(increasedHeightCounter)
