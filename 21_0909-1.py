# baekjoon 알고리즘 단계별 문제
# 입출력과 사칙연산
# 곱셈 응용 -> 곱셈의 과정 표시

num1 = int(input())
num2 = int(input())

temp = [(num2 % 10), int((num2 % 100) * 0.1) , int(num2 / 100)]

num3 = num1 * temp[0]
num4 = num1 * temp[1]
num5 = num1 * temp[2]

print(num3)
print(num4)
print(num5)
print(num1 * num2)