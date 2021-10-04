# baekjoon 알고리즘 단계별 문제
# 정렬
# 통계학(2108번)
import sys
from collections import Counter

N = int(input())
l = []

for i in range(N):
    l.append(int(sys.stdin.readline()))

avg = (sum(l) / N)
print(round(avg))  # round 반올림!

l.sort()  # 오름차순으로 정렬

print(l[len(l) // 2])

cnt_l = Counter(l).most_common()
if len(cnt_l) > 1 and cnt_l[0][1]==cnt_l[1][1]: #최빈값 2개 이상
    print(cnt_l[1][0])
else:
    print(cnt_l[0][0])

print(max(l)-min(l))


    




