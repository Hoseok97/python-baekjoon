# baekjoon 알고리즘 단계별 문제
# 재귀
# 팩토리얼(10872번)

def Factorial(n):
    answer = 1
    if n > 0:
           answer = n * Factorial(n-1)
    return answer

N = int(input())
print(Factorial(N))