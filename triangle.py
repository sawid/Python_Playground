inp = int(input())
if inp % 2 == 0:
    row = inp - 1
    for x in range(int(inp / 2)):
        for y in range(row):
            if y == ((int(row / 2) + 1) - (x) ) - 1 or y == ((int(row / 2) + 1) + (x)) - 1: 
                print("*", end="")
            else:
                print("-", end="")
        print()
    for x in range(int(inp / 2) - 1, -1, -1):
            for y in range(row):
                if y == ((int(row / 2) + 1) - (x) ) - 1 or y == ((int(row / 2) + 1) + (x)) - 1: 
                    print("*", end="")
                else:
                    print("-", end="")
            print()
else:
    row = inp
    for x in range(int(inp / 2)):
        for y in range(row):
            if y == ((int(row / 2) + 1) - (x) ) - 1 or y == ((int(row / 2) + 1) + (x)) - 1: 
                print("*", end="")
            else:
                print("-", end="")
        print()
    for x in range(int(inp / 2), -1, -1):
            for y in range(row):
                if y == ((int(row / 2) + 1) - (x) ) - 1 or y == ((int(row / 2) + 1) + (x)) - 1: 
                    print("*", end="")
                else:
                    print("-", end="")
            print()