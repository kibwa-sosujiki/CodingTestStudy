import heapq
import sys

N = int(sys.stdin.readline().strip()) #연산 개수
heap=[]
# x : 0이면 가장 작은 값 출력하고 그 값 제거, 자연수면 x라는 값 추가
# 입력 0이면 주어진 횟수 만큼 출력, 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력
for i in range(N):
    x=int(sys.stdin.readline().strip()) 
    print("X:", x)
    if x == 0:
        if len(heap)==0:
            print("출력:",0)
        else:
            k=heapq.heappop(heap)
            print("출력:",k)
            print("heap:", heap)
    elif x>0 :
        heapq.heappush(heap, x)
        print("heap:", heap)

