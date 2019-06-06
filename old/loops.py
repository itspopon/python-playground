amazingString = "fecking heck! it's time!"
amazingNumbers = "0,1461,141,111,4978497,1491"

# no need to add -1 since len() only goes until the last index
# for i in range(0, len(amazingString)):
#     print(amazingString[i],end="-")

cleanedNumbers = "";

# for i in range(0, len(amazingNumbers)):
#     if amazingNumbers[i] in "0123456789":
#         cleanedNumbers += amazingNumbers[i]

for char in amazingNumbers:
    if char in "0123456789":
        cleanedNumbers += char

#print(cleanedNumbers)

for i in range(0,100,7):
    print(i)