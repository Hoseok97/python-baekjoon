# baekjoon 알고리즘 단계별 문제
# 그리디 알고리즘
# ATM(11399번)

import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
time = []

p.sort()

time.append(p[0])

for i in range(1,N):
    time.append(p[i]+time[i-1])
    
print(sum(time))
    
