# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# 연속합(1912번)

import sys
input = sys.stdin.readline 

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))