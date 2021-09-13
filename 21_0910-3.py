# baekjoon 알고리즘 단계별 문제
# while문 활용
# 더하기 사이클
num = input()
count = 0

if int(num) < 10:
        num_1 = 0
        num_2 = num
else:
    num_1 = int(num[0])
    num_2 = int(num[1])    

while 1:
    sum = 0
    sum = int(num_1) + int(num_2)
    R = ((int(num_2) * 10) + (sum % 10))
    count+=1
    if R == int(num):
        break
    else:
        if R < 10:
            num_1 = 0
            num_2 = R
        else:
            num_1 = str(R)[0]
            num_2 = str(R)[1]
        

print(count)

# 더 간결한 정답
# num = int(input())
# check = num
# new_num = 0
# temp = 0
# count = 0
# while True:
#     temp = num//10 + num%10
#     new_num = (num%10)*10 + temp%10
#     count += 1
#     num = new_num
#     if new_num == check:
#         break
# print(count)