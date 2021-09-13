# baekjoon 알고리즘 단계별 문제
# 배열 활용
# 최소, 최대

N = int(input())
A = list(map(int, input().split()))

# h = A[0]
# l = A[-1]

# for i in A:
#     if i > h:
#         h = i
    
# for z in A:
#     if z < l:
#         l = z

# print(l, end = ' ')
# print(h)

# 더 간단하게
max = max(A)
min = min(A)

print(max, end = ' ')
print(min)
            