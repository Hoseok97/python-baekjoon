# baekjoon 알고리즘 단계별 문제
# 정수론 및 조합론
# 최소공배수 (1934번)

import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    a,b = map(int,input().split())
    A,B = a,b
    while a!=0:
        b = b%a
        a,b = b,a   
        
    gcd = b
    lcm = A * B //b
    print(lcm)