# baekjoon 알고리즘 단계별 문제
# 스택
# 스택(10828번)

import sys
input = sys.stdin.readline

n = int(input())
stack=[]
# 파이썬에서는 따로 stack구조를 제공하지 않는다 따라서 list로 구현을 해보았다.
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])