# baekjoon 알고리즘 단계별 문제
# 브루트 포스
# 영화감독 숌(1436번)

N = int(input())
Jnum = 666
cnt=0

while(True):
    if "666" in str(Jnum) :
        cnt+=1
    if cnt == N :
        print(Jnum)
        break
    
    Jnum+=1

