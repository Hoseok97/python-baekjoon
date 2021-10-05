# baekjoon 알고리즘 단계별 문제
# 정렬
# 좌표 정렬하기(11650번)
import sys
input = sys.stdin.readline

N = int(input())
l = []

for i in range(N):
    x, y = map(int, input().split())
    l.append((x,y))

l.sort()

for i in range(N):
    print(l[i][0], l[i][1])

