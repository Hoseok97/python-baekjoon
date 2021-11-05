# baekjoon 알고리즘 단계별 문제
# 그리디 알고리즘
# 잃어버린 괄호(1541번)

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)