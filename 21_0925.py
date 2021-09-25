# baekjoon 알고리즘 단계별 문제
# 기본 수학2
# 골드바흐의 추측(9020번)

import math

def isPrime(num):
    if num == 1: return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False

    return True

T = int(input())

li = list(range(2,10001))
prime_li = []
for i in li:
    if isPrime(i):
        prime_li.append(i)

while T:
    n = int(input())
    h = int(n / 2)

    if h in prime_li:
        print(h, h)
    else:
        for i in range(1,h):
            if (h+i) in prime_li and (h-i) in prime_li and (h+i) + (h-i) == n:
                print((h-i), (h+i))
                break
            

    T -= 1