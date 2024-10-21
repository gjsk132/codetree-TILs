num = int(input())

pos_info = {}

move_cnt = 0

for i in range(num):
    num, pos = map(int,input().split())

    if not num in pos_info:
        pos_info[num] = pos
    elif pos_info[num] and not pos:
        move_cnt += 1
        pos_info[num] = 0
    elif not pos_info[num] and pos:
        move_cnt += 1
        pos_info[num] = 1

print(move_cnt)