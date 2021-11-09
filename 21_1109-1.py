# baekjoon 알고리즘 단계별 문제
# 정수론 및 조합론
# 검문 (2981번)

# import sys
# input = sys.stdin.readline

# N = int(input())
# nl = []
# arr = []
# m = []
# cnt = 1

# for _ in range(N):
#     nl.append(int(input()))
    
# nl.sort()
    
# for i in range(1,N):
#     arr.append(nl[i] - nl[i-1])
    
# arr.sort()

# for i in range(2,arr[0]+1):
#     if arr[0] % i == 0:
#         for j in range(1,len(arr)):
#             if arr[j] % i == 0:
#                 cnt += 1
#             else:
#                 continue
#         if cnt == len(arr):
#             m.append(i)
        
# print(m)

import sys
input = sys.stdin.readline

def getGcd(a, b):
	r = a % b
	while r != 0:
		a = b
		b = r
		r = a % b
	return b
	
N = int(input())

arr = []
for _ in range(N):
	arr.append(int(input()))
arr.sort() # 정렬을 안해주면 차이가 음수가 나올 수 있어서 getGcd에서 타입에러가 난다

gcd = arr[1] - arr[0]
for i in range(2, N):
	gcd = getGcd(gcd, arr[i]-arr[i-1])
	
sol = [gcd]
for i in range(2, int(gcd**0.5)+1):
# 절반까지만 검사, 제곱근이 아닐 경우 나누어 떨어지면 그 짝을 sol의 첫번째 원소로 집어넣고 마지막에 sol 출력
	if gcd % i == 0:
		print(i, end=' ')
		if i != gcd//i:
			sol.insert(0, gcd//i)
for num in sol:
	print(num, end=' ')
            

            

        
        
    
