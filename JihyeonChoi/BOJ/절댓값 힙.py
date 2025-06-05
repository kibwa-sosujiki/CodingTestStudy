# import sys
# import heapq

# #연산의 개수N
# N=int(sys.stdin.readline().strip())
# heap_abs=[]
# heap={}
# for _ in range(N):
#     x=int(sys.stdin.readline().strip())
#     if x!=0:
#         heapq.heappush(heap_abs,  abs(x))
#         if abs(x) not in heap:
#             heap[abs(x)] = []
#         heap[abs(x)].append(x)

#     else:
#         if len(heap_abs)==0:
#             print(0)
#         else: 
#             k=heapq.heappop(heap_abs)
#             heapq.heapify(heap[k])
#             l=heapq.heappop(heap[k])
#             print( l)
            
import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))  # 절댓값 우선, 값이 같으면 실제값 우선
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
