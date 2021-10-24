# baekjoon 알고리즘 단계별 문제
# 동적 계획법
# RGB 거리(1149번)

import sys
input = sys.stdin.readline

N = int(input())
RGB = []

for _ in range(N):
    RGB.append(list(map(int, input().strip().split())))

# 0 = red, 1 = green, 2 = blue
# i번째 RGB를 i-1의 자기 자신을 제외한 다른 색 중 최솟값 + i번째 자신값으로 바꾼다.


for i in range(1,N):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][1], RGB[i-1][0]) + RGB[i][2]

# 이 과정을 N번 반복하면 RGB[N-1]은 서로 색이 겹치지 않는 값 합으로 나타난다
# print(RGB[N-1])

# 그 중 최솟값 출력
print(min(RGB[N-1]))
