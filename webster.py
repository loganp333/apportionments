import math
from colorama import Fore, Back, Style, init
from decimal import Decimal, ROUND_HALF_UP
import copy
#print(Decimal(7.3).quantize(0, ROUND_HALF_UP))
init()
potentialDistricts = {}
discSQ = {}
standardD = 0
totalPop = 0
valArray = []
betaApportionment = 0
apporBackup = 0
def webster1():
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
        discSQ[key] = int(Decimal(value / standardD).quantize(0, ROUND_HALF_UP))
    
    for value in discSQ.values():
        betaApportionment += value


    apporBackup = copy.deepcopy(betaApportionment)

    global apportionmentFound
    apportionmentFound = False

    while apportionmentFound != True:
        if betaApportionment == seatCount:
            apportionmentFound = True
            break
        elif betaApportionment < seatCount:
            standardD -= 1
            
            for key, value in potentialDistricts.items():
                discSQ[key] = int(Decimal(value / standardD).quantize(0, ROUND_HALF_UP))

            betaApportionment = 0

            for value in discSQ.values():
                betaApportionment += int(value)
            
            if betaApportionment == seatCount:
                apportionmentFound = True
                break
            else:
                betaApportionment = copy.deepcopy(apporBackup)
                continue

        elif betaApportionment > seatCount:
            standardD += 1
            for key, value in potentialDistricts.items():
                discSQ[key] = int(Decimal(value / standardD).quantize(0, ROUND_HALF_UP)) 

            betaApportionment = 0

            for value in discSQ.values():
                betaApportionment += value
            
            if betaApportionment == seatCount:
                apportionmentFound = True
                break
            else:
                betaApportionment = copy.deepcopy(apporBackup)
                continue
        else:
            print("???")

    print("Webster's Apportionment")
    print(Fore.MAGENTA + "---------------------")
    print("\n" + Style.RESET_ALL)
    print("Modified SD" + Fore.MAGENTA + " -> " + Style.RESET_ALL + str(standardD))
    for key, value in discSQ.items():
        print(key + Fore.MAGENTA + " -> " + Style.RESET_ALL + str(value))
