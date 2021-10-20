# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# 신나는 함수 실행(9184번)

import sys
input = sys.stdin.readline

def w(a,b,c):
    if a <= 0 or b <= 0 or c <=0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    elif dp[a][b][c]:   # dp 값이 있으면 바로 반환! 시간 단축
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    
    
    return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while 1:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({},{},{}) = {}'.format(a, b, c, w(a,b,c)))