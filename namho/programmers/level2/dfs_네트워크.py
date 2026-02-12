#https://school.programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    answer = 0
    visited=[False]*n
    def dfs(node):
        visited[node] = True
        for i in range(len(computers[node])):
            if computers[node][i]==1 and not visited[i]:
                dfs(i) # 1이고 방문 안했으면 그 노드에서부터 dfs
    for i in range(n):
        if not visited[i]: #처음으로 방문안한 노드에서 시작
            answer+=1
            dfs(i)
            
    return answer