def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(c_num):
        visited[c_num]=True
        for neighbor in range(n):
            if computers[c_num][neighbor]==1 and visited[neighbor] == False:
                dfs(neighbor)
                
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer+=1
    
    
    return answer