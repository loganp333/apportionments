import math
import copy
from decimal import Decimal
from colorama import Fore, Back, Style, init
init()
potentialDistricts = {}
discSQ = {}
discLQ = {}
standardD = 0
totalPop = 0
valArray = []
biggest = []


def hamilton1():
    totalPop = 0
    global betaApportionment
    betaApportionment = 0
    x = 0
    print("\n")
    print("Enter The Details of The Districts in Order")
    print(Fore.RED + "-------------------------------------------")
    print("\n")
    print(Style.RESET_ALL) 

    discCount = int(input("Number of Districts: "))
    seatCount = int(input("Enter the Number of Seats (m) Available: "))

    while x < discCount:
        discName = input("District name: ")
        discPop = int(input("District population: "))
        potentialDistricts[discName] = discPop
        x += 1

    print("\n")
    for value in potentialDistricts.values():
        totalPop += value

    standardD = totalPop / seatCount

    for key, value in potentialDistricts.items():
        discSQ[key] = value / standardD

    discLQ = copy.deepcopy(discSQ)

    decimals = []

    for value in discSQ.values():
        decimals.append(int(value * 10) % 10)


    for key, value in discSQ.items():
        valArray.append(value)
        discLQ[key] = math.floor(value)


    betaApportionment = 0

    for value in discLQ.values():
        betaApportionment += value

    surplus = seatCount - betaApportionment
    y = 0


    while y < surplus:
        biggestVal = max(decimals)
        biggest.append(biggestVal)
        decimals.remove(biggestVal)
        y += 1

    print("\n")

    for key, value in discSQ.items():
        valDec = int(value * 10) % 10
        for x in biggest:
            if valDec == x:
                discLQ[key] = math.floor(value + 1)
            else:
                pass

    print("Hamilton's Apportionment")
    print(Fore.MAGENTA + "---------------------")
    print("\n" + Style.RESET_ALL)
    print("SD" + Fore.MAGENTA + " -> " + Style.RESET_ALL + str(standardD))
    for key, value in discLQ.items():
        print(key + Fore.MAGENTA + " -> " + Style.RESET_ALL + str(value))





