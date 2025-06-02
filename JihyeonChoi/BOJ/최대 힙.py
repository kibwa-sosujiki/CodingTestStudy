import sys 
import heapq

N = int(sys.stdin.readline().strip())
heap=[]
for _ in range(N):
    x=int(sys.stdin.readline().strip())
    if x == 0:
        if len(heap)==0:
            print(0)
        else:
            k=heapq.heappop(heap)
            print(-k)
    else:
        heapq.heappush(heap, -x)