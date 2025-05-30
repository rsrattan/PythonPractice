def divby5(listofNumbers):
    for num in listofNumbers:
        if num/5 == num//5:
            print(num)
divby5([10, 20, 33, 46, 55])