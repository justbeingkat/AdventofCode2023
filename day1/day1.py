inputText = open("input.txt", "r")
lines = inputText.readlines()

numberList = []

for line in lines:
    num = ""
    for char in line:
        if ":" > char > "/":
            num += char
    num = num[0] + num[-1]
    numberList.append(int(num))
print(numberList)
totalSum = sum(numberList)
print(totalSum)
