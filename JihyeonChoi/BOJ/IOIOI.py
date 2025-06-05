import sys

#첫째 줄에 N
#둘째 줄에 S의 길이 M
#셋째 줄에 S
#Pn : N+1 개의 I와 N개의 o가 교대로 나오는 문자열

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
S=sys.stdin.readline()

i=0
cnt=0
answer =0 

while i<M-1:
    if S[i]=="I" and S[i+1]=="O" and S[i+2]=="I":
        cnt+=1
        i+=2
        if cnt==N:
            answer+=1
            cnt-=1 #다음 IOI가 이어지면 또 cnt+=1하면 N 돼서 answer+=1 되도록 
    else:
        i+=1
        cnt=0

print (answer)

