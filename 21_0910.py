# baekjoon 알고리즘 단계별 문제
# if문 활용
# 45 일찍 알람 시계
H,M = map(int, input().split())
m = M - 45
h = H
if m < 0:
    m += 60
    h -= 1
    if h < 0:
        h += 24

print(h, end = ' ')
print(m)        