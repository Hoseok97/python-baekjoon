# baekjoon 알고리즘 단계별 문제
# 기본 수학1
# 벌집 (2292번)

N = int(input())
first = 1
plus = 6
door = 1

if N == 1:
    print(1)    
else:
    while True:

        first = first + plus
        door += 1

        if N <= first:
            print(door)
            break

        plus += 6
