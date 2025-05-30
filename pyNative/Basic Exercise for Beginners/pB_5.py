def checkFirstLast(listOfNumbers):
    if listOfNumbers[0] == listOfNumbers[-1]:
        print(True)
    else:
        print(False)


numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False

checkFirstLast(numbers_x)
checkFirstLast(numbers_y)