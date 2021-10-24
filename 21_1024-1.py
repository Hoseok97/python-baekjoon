# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# 파도반 수열(9461번)

import sys
input = sys.stdin.readline

p = [0] * 10000
p[0] = 1 
p[1] = 1
p[2] = 1
p[3] = 2
p[4] = 2
p[5] = 3
p[6] = 4
p[7] = 5
p[8] = 7
p[9] = 9

N = int(input())
for _ in range(N):
    n = int(input())
    for i in range(10,n+1):
        p[i] = p[i-1] + p[i-5]
    print(p[n-1])