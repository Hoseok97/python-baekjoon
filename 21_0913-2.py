# baekjoon 알고리즘 단계별 문제
# 배열 활용
# 평균은 넘겠지

N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')




