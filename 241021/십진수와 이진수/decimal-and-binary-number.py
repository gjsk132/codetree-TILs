N = list(input())

num = 0

length = len(N)

for i, v in enumerate(N):
    if v == "1":
        num += pow(2, length-i-1)


print(str(bin(num*17))[2:])