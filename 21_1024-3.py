# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# 정수 삼각형(1932번)

import sys
input = sys.stdin.readline

N = int(input())
rec = []

for _ in range(N):
    rec.append(list(map(int, input().strip().split())))

for i in range(2,N):
    rec[i][0] += rec[i-1][0]
    rec[i][-1] += rec[i-1][-1]
    for j in range(1,i):
        rec[i][j] = max(rec[i-1][j-1], rec[i-1][j]) + rec[i][j]

print(max(rec[N-1]) + rec[0][0])
    
# if문을 사용한 쫌 더 심플한 코드

# n = int(input())

# t_list = []

# for _ in range(n):
#     t_list.append(list(map(int, input().split())))


# for i in range(1,n):
#     for j in range(i+1):
#         if j == 0:
#             t_list[i][j] = t_list[i][j] + t_list[i-1][j]
#         elif i == j:
#             t_list[i][j] = t_list[i][j] + t_list[i-1][j-1]
#         else:
#             t_list[i][j] = max(t_list[i][j]+t_list[i-1][j],
#                                t_list[i][j]+t_list[i-1][j-1])

# print(max(t_list[n-1]))
