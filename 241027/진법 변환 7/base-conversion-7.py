x, y = map(int,input().split("."))
x = bin(x)+"."
x = list(x[2:])

y = float(y/10**len(str(y)))

for _ in range(4):
    y *= 2
    
    if y >= 1:
        x.append("1")
        y-=1
    else:
        x.append("0")

print(*x, sep="")