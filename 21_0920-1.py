# baekjoon 알고리즘 단계별 문제
# 기본 수학1
# 달팽이는 올라가고 싶다(2869)

A, B, V = map(int, input().split())

day = ((V-B) / (A-B))

print(int(day) if day == int(day) else int(day) + 1)
