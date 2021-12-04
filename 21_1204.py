# baekjoon 알고리즘 단계별 문제
# 스택
# 제로(10773번)

N = int(input())
z_num = []
for i in range(N):
    num = int(input())
    if num == 0:
        z_num.pop()
    else:
        z_num.append(num)
print(sum(z_num))