from jefferson import jefferson1
from adams import adams1
from hamilton import hamilton1
from webster import webster1
q = False

print(
'''
+----------------------------------------+----------+
|Python Apportionment Algorithm | By Logan Phillips |
+----------------------------------------+----------+
'''
    )
print("\n")

while q != True:
    res = input("Type Q to exit | Type a method: ").lower()

    if res == "hamilton" or res == "hamiltons" or res == "hamilton's":
        hamilton1()
    elif res == "webster" or res == "websters" or res == "webster's":
        webster1()
    elif res == "adam" or res == "adams" or res == "adam's":
        adams1()
    elif res == "jefferson" or res == "jeffersons" or res == "jefferson's":
        jefferson1()
    elif res == "q" or res =="quit" or res == "exit":
        break
    else:
        print("Invalid statement. Please try rewriting your response.")
        continue