# baekjoon 알고리즘 단계별 문제
# 정렬
# 소트인사이드(1427번)

n = int(input())
 
li = []
for i in str(n):
    li.append(int(i))
# li = list(map(int,str(n))) 으로 변경가능
    
li.sort(reverse=True) # 내림차순
 
for i in li:
    print(i,end='')