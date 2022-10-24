import datetime
inp = input().split(" ")
print((datetime.datetime(2009,int(inp[1]),int(inp[0]))).strftime("%A"))