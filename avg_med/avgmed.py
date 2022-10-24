sum = 0

inp = input().split(" ")

for i in inp:
    sum += int(i)

if len(inp) % 2 == 0:
    med_index = (len(inp) + 1) / 2
    med = (int(inp[int(med_index + 0.5) - 1]) + int(inp[int(med_index - 0.5) - 1])) / 2
else :
    med = inp[int((len(inp) + 1) / 2) - 1]

print("{} {}".format(med,sum/len(inp)))