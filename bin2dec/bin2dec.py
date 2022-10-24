inp = input()

listOfNumber = [*inp]
listOfNumber = [int(x) for x in listOfNumber]

dec = 0
powNumber = 0

for i in range(len(listOfNumber) - 1, -1, -1):
    if listOfNumber[i] == 1:
        dec += (2 ** powNumber) * listOfNumber[i]
    powNumber += 1

print(dec)