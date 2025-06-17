import sys

N = int(sys.stdin.readline()) 
num=666
cnt = 0

for i in range(666, 10000000):
    if "666" in str(i):
        num = i
        cnt+=1
        if cnt == N :
            break
        
print(num)