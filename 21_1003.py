# baekjoon 알고리즘 단계별 문제
# 정렬
# 수 정렬하기 2(2751번)

import sys

N = int(input())
list_num = []

for i in range(N):
    list_num.append(int(sys.stdin.readline()))

for i in sorted(list_num):  # stored 오름차순으로 정렬
    sys.stdout.write(str(i)+'\n')
    