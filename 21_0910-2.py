# baekjoon 알고리즘 단계별 문제
# for문 활용
# X 보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i < X:
        print(i, end=" ")