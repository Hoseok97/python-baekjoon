# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# 피보나치 함수(1003번)
import sys
input = sys.stdin.readline

def fibo (n):
    global z_cnt, o_cnt
    if n == 0:
        z_cnt += 1
        return 0
    elif n == 1:
        o_cnt += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

T = int(input())

for i in range(T):
    z_cnt = 0
    o_cnt = 0
    num = int(input())
    fibo(num)
    print(z_cnt, o_cnt)

# 시간 단축을 위해 0,1 이 0,1,2 일때 값 미리 저장 한 답

# zero = [1, 0, 1]
# one = [0, 1, 1]

# def fibonacci(num):
#     length = len(zero)
#     if num >= length:
#         for i in range(length, num+1):
#             zero.append(zero[i-1] + zero[i-2])
#             one.append(one[i-1] + one[i-2])
#     print('{} {}'.format(zero[num], one[num]))

# T = int(input())
    
# for _ in range(T):
#     fibonacci(int(input()))