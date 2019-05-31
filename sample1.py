
def evenCal(inputNum):
    if(int(inputNum) * 2) < 10:
        return inputNum*2
    else:
        outChar = str(inputNum*2)
        return int(outChar[0]) + int(outChar[1])

inputNum = 8
print(evenCal(inputNum))
