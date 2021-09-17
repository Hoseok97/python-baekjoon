# baekjoon 알고리즘 단계별 문제
# 기본 수학1
# 손익분기점 (1712번)

A, B, C = map(int, input().split())

# 내 답안
# n = 0

# while 1:
#         n += 1
#         if (A + (B * n)) < C * n:
#             print(n)
#             break
#         elif B >= C:
#             print('-1')
#             break
# A가 숫자가 커질 경우 run 타임이 길어져 에러가 난다.

# 답
if B >= C:
    print('-1')
else:
    print(A//(C-B)+1)
        

        

