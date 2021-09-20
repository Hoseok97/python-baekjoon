# baekjoon 알고리즘 단계별 문제
# 기본 수학1
# 설탕 배달(2839)

N = int(input())

bag = 0
while N >= 0 :
    if N % 5 == 0 :  
        bag += (N // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    N -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)