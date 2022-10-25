def ahCounter(strData) :
    count = 0
    for i in strData:
        if i != "h":
            count += 1
    return count
inpAct = input()
inpReq = input()

if ahCounter(inpAct) >= ahCounter(inpReq):
    print("go")

else :
    print("no")
    