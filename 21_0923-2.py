# baekjoon 알고리즘 단계별 문제
# 기본 수학2
# 베르트랑 공준(4948번)

# 내 답안
# 시간 초과로 실패
# import math

# from math import sqrt

# while 1:
#     n = int(input())
#     if n == 0:
#         break
    
#     cnt = 0

#     for i in range(n + 1, n * 2 + 1):
#         if i == 1:
#             continue

#         elif i == 2:
#             cnt += 1
#             continue

#         else:
#             for j in range(2, int(sqrt(i)+1)):
#                 if i % j == 0:
#                     break
#             else:
#                 cnt += 1

#     print(cnt)

# 구글링 하여 수정한 답안
# 미리 123456의 2배인 2246912 사이 소수를 구하여 시간 단축

import math

def isPrime(num):
    if num == 1: return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False

    return True


li = list(range(2,246912))
prime_li = []
for i in li:
    if isPrime(i):
        prime_li.append(i)

while(1):
    answer = 0
    n = int(input())
    if n == 0: break

    for i in prime_li:
        if n < i <= n*2:
            answer += 1

    print(answer)



