number = "9,54,1212,456,852"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber += number[i]
else:
    print(cleanedNumber)
