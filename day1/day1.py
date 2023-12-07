inputText = open("input.txt", "r")
lines = inputText.readlines()

numberDict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

numberList = []

for line in lines:
    num = ""
    newstring = ""
    for char in line:
        if "/" < char < ":":
            num += char
        else:
            newstring += char
            for number in numberDict:
                if number in newstring:
                    num += str(numberDict[number])
                    newstring = newstring[-1]
    print(num)
    num = num[0] + num[-1]
    numberList.append(int(num))
totalSum = sum(numberList)
print(totalSum)
