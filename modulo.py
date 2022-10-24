listData = []
for x in range(10):
    inp = (int(input()) % 42)
    if (inp) not in listData:
        listData.append(inp)
print(len(listData))