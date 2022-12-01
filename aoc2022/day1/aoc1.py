input = open("input.txt")
calorieList = []
for line in input:
    calorieList.append(line)


def solutions():
    maxCalories = [0, 0, 0]
    currentCalories = 0

    for line in calorieList:
        if line != '\n':
            currentCalories += int(line)
        else:
            if currentCalories > min(maxCalories):
                maxCalories.remove(min(maxCalories))
                maxCalories.append(currentCalories)
            currentCalories = 0

    return maxCalories


print({max(solutions())})
print({sum(solutions())})
