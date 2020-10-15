import random

coinList = []
numOfH = 0
numOfT = 0

numOfStreaks = 0

for x in range(10000):
    if (random.randint(0, 1) == 0):
        coinList.append("H")
    else:
        coinList.append("T")

for items in coinList:
    if (numOfH == 6 or numOfT == 6):
        numOfStreaks += 1
        numOfH = 0
        numOfT = 0

    if items == "H":
        numOfH += 1
        numOfT = 0
    else: 
        numOfT += 1
        numOfH = 0

print(numOfStreaks)
# print(coinList)