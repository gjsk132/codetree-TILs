x, y = map(int,input().split("."))
x = bin(x)+"."
x = list(x[2:])

length = 10**len(str(y))

for _ in range(4):
    if not y:
        x.append("0")
        continue
    
    y *= 2
    
    x.append(str(y//length))
    y %= length

print(*x, sep="")