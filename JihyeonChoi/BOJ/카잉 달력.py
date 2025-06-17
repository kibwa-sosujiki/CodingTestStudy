import sys
# 데이터의 입력을 나태내는 정수 T
T = int(sys.stdin.readline())

for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    
    #x를 기준으로 맞춰보자
    year = x
    found = False
    while year <= M*N:
        if (year-1)%N+1 == y:
            found=True
            print(year)
            break
        year+=M

    if not found:
        print(-1)




