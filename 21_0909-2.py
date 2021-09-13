# baekjoon 알고리즘 단계별 문제
# if문 활용
# 두 수 비교하기

A,B = map(int, input().split()) #map 함수로 두개의 문자를 int type으로 변환

if A < B:
    print('<')
elif  A > B:
    print('>')
else:
    print('==')
