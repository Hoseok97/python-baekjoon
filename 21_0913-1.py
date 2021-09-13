# baekjoon 알고리즘 단계별 문제
# 배열 활용
# 평균

N = int(input())
A = list(map(int, input().split()))
sum = float()

for i in A:
    sum += float(i / max(A)) * 100
    

print(float(sum/N))