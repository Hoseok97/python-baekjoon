# baekjoon 알고리즘 단계별 문제
# 백트래킹
# 연산자 끼워넣기(14888번)
import sys
input = sys.stdin.readline

def cal(num, idx, add, sub, mul, div):
    global N, maxr, minr
    if idx == N:
        maxr = max(num, maxr)
        minr = min(num, minr)
        return
    else:
        if add:
            cal(num + n_list[idx], idx+1, add-1, sub, mul, div)
        if sub:
            cal(num - n_list[idx], idx+1, add, sub-1, mul, div)
        if mul:
            cal(num * n_list[idx], idx+1, add, sub, mul-1, div)
        if div:
            cal(-(-num // n_list[idx]) if num<0 else num // n_list[idx], idx+1, add, sub, mul, div-1)

N = int(input().strip())
n_list = list(map(int, input().strip().split()))
p, m, x, d = map(int, input().strip().split())
maxr = -sys.maxsize - 1
minr = sys.maxsize
cal(n_list[0],1,p,m,x,d)
print(maxr)
print(minr)



    