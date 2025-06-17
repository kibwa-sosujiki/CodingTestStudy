import sys

N = int(sys.stdin.readline())
point = []

for i in range(N):
    point.append(list(map(int, sys.stdin.readline().split()))) 

temp1=0
temp2=0
for i in range(N):
    if i==N-1:
        temp1 += point[i][0]*point[0][1]
        temp2 += point[i][1]*point[0][0]
    else : 
        temp1 += point[i][0]*point[i+1][1]
        temp2 += point[i][1]*point[i+1][0]

print(abs((temp2-temp1)/2))