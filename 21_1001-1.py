# baekjoon 알고리즘 단계별 문제
# 브루트 포스
# 분해합(2231번)

N = int(input())


for i in range(1,N+1):
    num = 0
    for j in str(i):
        num += int(j)
    if num + i == N:
        print(i)
        break
    elif i == N:
        print(0)
