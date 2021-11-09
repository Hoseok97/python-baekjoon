# baekjoon 알고리즘 단계별 문제
# 정수론 및 조합론
# 다리 놓기(1010번)

import sys
input = sys.stdin.readline

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


N = int(input())
bridge = []

for _ in range(N):
    n, m = map(int, input().split())
    bridge.append(factorial(m) // (factorial(n) * factorial(m - n)))

for i in range(len(bridge)):
    print(bridge[i])
    
    