# baekjoon 알고리즘 단계별 문제
# 기본 수학2
# 소수 찾기(1974번)

N = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                error += 1

        if error == 0:
            sosu += 1
    

print(sosu)
            
