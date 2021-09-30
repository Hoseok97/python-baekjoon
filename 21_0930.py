# baekjoon 알고리즘 단계별 문제
# 브루트 포스
# 블랙잭(2798번)

N, M = map(int, input().split())
C = list(map(int, input().split()))

sum = 0

for i in range(0, len(C)- 2):
    for j in range(i+1, len(C) - 1):
        for k in range(j+1, len(C)):
            if C[i] + C[j] + C[k] > M:
                continue
            else:
                sum = max(sum, C[i]+C[j]+C[k]) # sum, C[i]+C[j]+C[k]를 비교하여 더 큰 값을 sum에 입력

print(sum)

