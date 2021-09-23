# baekjoon 알고리즘 단계별 문제
# 기본 수학2
# 소수 구하기 (1929번)
import math

def sosu(num):
    if num == 1:
        return False
    
    sq = int(math.sqrt(num))           

    for i in range(2, sq+1):
        if num % i == 0:
            return False

    return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if sosu(i):
        print(i)




    
        
