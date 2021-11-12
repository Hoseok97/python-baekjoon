# baekjoon 알고리즘 단계별 문제
# 정수론 및 조합론
# 약수 (1037번)

import sys
input = sys.stdin.readline

n = int(input())
mea = list(map(int, input().split()))
a = min(mea)
b = max(mea)
print(a*b)