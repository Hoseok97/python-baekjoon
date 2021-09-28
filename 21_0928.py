# baekjoon 알고리즘 단계별 문제
# 재귀
# 하노이 탑 이동 순서(11729번)

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

    

N = int(input())
print(2**N-1)
hanoi(N, 1, 3)
