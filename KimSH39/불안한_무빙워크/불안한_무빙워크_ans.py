from collections import deque

n, k = map(int, input().split())

# deque는 양쪽 끝에서 삽입 삭제가 빠른 자료구조
dur = deque(map(int, input().split()))
human = deque([False] * n)

step = 0

# 내구도가 0인 칸의 수가 k개 이상이 되면 break로 종료
while True:
    step += 1

    # 1. 무빙워크 한 칸 회전
    dur.rotate(1)

    # 1-1. 위에 있던 사람도 같이 회전
    human.rotate(1)

    # 1-2. n 밖으로 나가면 사람 내려감
    # 즉, 마지막 칸을 비워진 칸으로 처리하는 것
    human[-1] = False

    # 2. 만약 무빙워크에 사람이 있고, 앞으로 한 칸 이동할 수 있으면 이동함

    # 2-1. 이동은 뒤에 있는 사람부터(그래야 연쇄적으로 이동시킬 수 있기 때문)
         # 맨 마지막 칸은 고려 X, 어차피 사람 있다면 내려서 비울 칸이니까

    # 끝 바로 앞 칸부터 0까지(range는 끝값 미포함이라 -1까지 가야 0 포함됨) -1씩
    for i in range(n-2, -1, -1):

        # 즉, 해당 칸에 사람이 있고, 앞에 사람 없거나, 앞 칸의 안정성이 1 이상일 때 이동함
        if human[i] and not human[i+1] and dur[i+1] > 0:
            human[i] = False
            human[i+1] = True
            dur[i+1] -= 1
            
    human[-1] = False

    # 3. 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람 올림
    if human[0] == False and dur[0] > 0:
        human[0] = True
        dur[0] -= 1

    # 4. 안정성이 0인 판이 k개가 되면 종료
    if dur.count(0) >= k:
        break

print(step)