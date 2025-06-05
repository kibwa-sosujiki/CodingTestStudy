import sys

T=int(sys.stdin.readline().strip())

for i in range(T):
    n=int(sys.stdin.readline().strip())
    wears={}

    for _ in range(n):
        name, type = sys.stdin.readline().strip().split()
        if type in wears:
            wears[type].append(name)
        else: wears[type]=[name]

    count=1
    # 각각의 type을 입거나 입지 않기 그리고 전체 알몸되는 상황 빼기
    for type in wears:
        count*=(len(wears[type])+1)
    print(count-1)
    