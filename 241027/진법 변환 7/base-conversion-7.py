x, y = map(str,input().split("."))
x = bin(int(x))+"."
x = list(x[2:])

y = float("0."+y)

for _ in range(4):
    y *= 2
    if y >= 1:
        x.append("1")
        y-=1
    else:
        x.append("0")

print(*x, sep="")