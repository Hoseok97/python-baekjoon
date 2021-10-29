# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# 포도주 시식(2156번)

import sys
input = sys.stdin.readline


N = int(input())
dp = [0 for _ in range(N+3)]
g = [0 for _ in range(N+3)]
for k in range(1,N+1):
    g[k] = int(input())


dp [1] = g[1]
dp [2] = g[1] + g[2]

for i in range(3, N+1):
    dp[i] = max(dp[i - 1], dp[i - 3] + g[i - 1] + g[i], dp[i - 2] + g[i]) 

print(dp[N])

