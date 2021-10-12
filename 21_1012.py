# baekjoon 알고리즘 단계별 문제
# 백트래킹
# N 과 M-4(15652번)

n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if len(s) > 0:
            if s[-1] > i:
                continue
        s.append(i)
        dfs()
        s.pop()
           
dfs()
