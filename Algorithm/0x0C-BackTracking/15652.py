import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []

def sol(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n+1):
        s.append(i)
        sol(i)
        s.pop()

sol(1)