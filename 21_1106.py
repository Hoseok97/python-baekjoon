# baekjoon 알고리즘 단계별 문제
# 그리디 알고리즘
# 동전 0 (11047번)

N,K = map(int, input().split())

Ai = [] # 동전의 가치 저장할 리스트 선언
count = 0 # 동전의 개수를 저장할 변수

i = N-1

for _ in range(N):
  Ai.append(int(input()))

while K != 0:
  count += K//Ai[i] # 동전의 개수를 저장
  K %= Ai[i] # 동전의 가치로 나눈 나머지를 저장
  i -= 1 # 인덱스를 감소시킨다.

print(count)