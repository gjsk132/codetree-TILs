array_cnt, num = map(int,input().split())

array = sorted(list(map(int,input().split())))

limit = len(array)
pos = 0

while pos < limit and num >= array[pos]:
    num += 1
    pos += 1

print(num)