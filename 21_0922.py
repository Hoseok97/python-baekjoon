# baekjoon 알고리즘 단계별 문제
# 기본 수학2
# 소수(2581)

M = int(input())
N = int(input())

sosu = []

for num in range(M,N+1):
    error = 0
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                error += 1
                break

        if error == 0:
            sosu.append(num)

if len(sosu) > 0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
