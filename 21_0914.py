# baekjoon 알고리즘 단계별 문제
# 함수
# 셀프 넘버
sn = []

for i in range(1, 10):
    sn.append(2*i)

for i in range(10, 100):
    sn.append(i + int(i / 10) + int(i % 10))

for i in range(100, 1000):
    sn.append(i + int(i % 10) + int(i / 100) + int((i % 100) / 10))

for i in range(1000, 10001):
    sn.append(i + int(i / 1000) + int(i % 10) + int((i / 100) % 10) + int((i % 100) / 10))



for i in range(1, 10000):
    if i in sn:
        continue
    else:
        print(i)

# 문자열로 더 쉽게 구하는 방법
# numbers = list(range(1, 10_001))
# remove_list = []  # 이후에 삭제할 숫자 list
# for num in numbers :
#     for n in str(num):
#         num += int(n)  # 생성자가 있는 숫자
#     if num <= 10_000:  # 10,000보다 작거나 같을 때만,
#         remove_list.append(num)  # append: 리스트에 요소를 추가할 때

# for remove_num in set(remove_list) :  # set 으로 중복값 제거
#     numbers.remove(remove_num)
# for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
#     print(self_num)






