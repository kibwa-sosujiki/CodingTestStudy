import sys

N = int(sys.stdin.readline()) # 이동할 채널 번호
M = int(sys.stdin.readline()) #고장난 버튼의 개수
current = 100

if M > 0:  #고장난 버튼 번호
    broken = list(sys.stdin.readline().split())
else:
    broken = []
    
# 현재에서 +- 버튼만으로 이동 
min_press = abs(N-current)

# 버튼을 누를 수 있는지?
def can_press(N):
    for i in str(N):
        if i in broken:
            return False 
    return True

#전체돌면서
for i in range(1000000):
    if can_press(i):
        press = len(str(i))+abs(i-N)
        min_press = min(press, min_press)

print(min_press)