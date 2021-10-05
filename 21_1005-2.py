# baekjoon 알고리즘 단계별 문제
# 정렬
# 단어정렬(1181번)

import sys

N = int(sys.stdin.readline())
word = []

for i in range(N):
    word.append(str(sys.stdin.readline().rstrip()))

set_word = set(word)      # set으로 바꾸면서 중복값 제거
word = list(set_word)

word.sort()               # 사전 순 정렬 
word.sort(key=len)        # 크기 순 정렬


for i in word:
    print(i)

