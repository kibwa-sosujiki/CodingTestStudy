import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works] #음수로 바꿈 
    heapq.heapify(works)  #음수로 제일 작은게 제일 큰거니까 최대 힙으로 만들기
    
    for _ in range(n):
        max = heapq.heappop(works) # 음수니까 제일 작은거 선택하는게 실제론 제일 큰거임    
        heapq.heappush(works, max+1) #현재 음수니까 +1
    return sum(x ** 2 for x in works)
