import math
import copy
from colorama import Fore, Back, Style, init
init()
potentialDistricts = {}
discSQ = {}
discHQ = {}
standardD = 0
totalPop = 0
valArray = []
betaApportionment = 0

def adams1():
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

    discHQ = copy.deepcopy(discSQ)


    for key, value in discSQ.items():
        valArray.append(value)
        discHQ[key] = math.ceil(value)


    for value in discHQ.values():
        betaApportionment += value

    global apportionmentFound
    apportionmentFound = False

    while apportionmentFound != True:
        standardD += 1

        for key, value in potentialDistricts.items():
            discHQ[key] = math.ceil(value / standardD)

        for value in discHQ.values():
            betaApportionment += math.ceil(value)

        if betaApportionment == seatCount:
            apportionmentFound = True
            break
        else:
            betaApportionment = 0
            continue
    print("Adam's Apportionment")
    print(Fore.MAGENTA + "---------------------")
    print("\n" + Style.RESET_ALL)
    print("Modified SD" + Fore.MAGENTA + " -> " + Style.RESET_ALL + str(standardD))
    for key, value in discHQ.items():
        print(key + Fore.MAGENTA + " -> " + Style.RESET_ALL + str(value))
