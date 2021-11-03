# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# 평범한 배낭(12865번)

import sys
input = sys.stdin.readline

N, K= map(int,input().split())
wv = [[0,0]]
dp = [[0]*(K+1)for _ in range(N+1)]

for _ in range(N):
    wv.append(list(map(int, input().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        w = wv[i][0]
        v = wv[i][1]

        if j < w:
                dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])

