# baekjoon 알고리즘 단계별 문제
# 배열 활용
# 최댓값

arr = []
for i in range(9):
    arr.append(int(input()))
 
max = max(arr)
print()
print(max)
idx = arr.index(max)
print(idx+1)