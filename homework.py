inp = input().split(";")

count = 0

for i in inp:
    if "-" in i:
        num = i.split("-")
        count += (int(num[1]) - int(num[0])) + 1
    else :
        count += 1

print(count)