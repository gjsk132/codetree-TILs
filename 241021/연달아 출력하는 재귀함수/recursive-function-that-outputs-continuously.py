num = int(input())

answer = []

while num > 0:
    answer.append(num)
    num //= 3

print(" ".join(map(str,(reversed(answer)))))