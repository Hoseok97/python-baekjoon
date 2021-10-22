# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# 01타일 (1904번)

import sys
input = sys.stdin.readline

N = int(input())

t = [0] * 1000001
t[1] = 1
t[2] = 2

for i in range(3,N+1):
    t[i] = (t[i-1] + t[i-2]) % 15746

print(t[N])


