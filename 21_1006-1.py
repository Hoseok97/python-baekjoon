# baekjoon 알고리즘 단계별 문제
# 정렬
# 나이순 정렬(10814번)

import sys

N = int(sys.stdin.readline())

l = []

for i in range(N):
    l.append(list(sys.stdin.readline().rstrip().split()))

l.sort(key=lambda x: int(x[0]))  # 첫번째 인덱스 기준 sort 정렬

for i in range(N):
    print(l[i][0], l[i][1])

