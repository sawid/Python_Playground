def checkExistChar(strList, charToCheck):
    for x in range(len(strList)):
        if strList[x][1] == charToCheck:
            return x
    return -1

inp = input().split(" ")
commission = []
while inp[0] != "-1":
    if checkExistChar(commission, inp[1]) != -1:
        if inp[2] == "right":
            commission[checkExistChar(commission, inp[1])][2] = True
            commission[checkExistChar(commission, inp[1])][0] += int(inp[0])
        else :
            commission[checkExistChar(commission, inp[1])][0] += 20
    else :
        if inp[2] == "right":
            commission.append([int(inp[0]), inp[1], True])
        else :
            commission.append([0, inp[1], False])
    print(commission)
    inp = input().split(" ")
print(commission)