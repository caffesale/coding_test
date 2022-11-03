
# 인접 행렬로 구현한 graph일 때의 dfs
# 방문여부를 뜻하는 visited parameter가 별도로 필요없다.

n,m = map(int, input().split())

graph = []
for i in range(n):
	graph.append(list(map(int, input())))

def dfs(x,y):
	# 범위를 벋어나면 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
      return False
	# 해당 노드를 방문하지 않았다면 방문처리
	if graph[x][y] == 0:
      grpah[x][y] = 1
      dfs(x-1,y)
      dfs(x, y-1)
      dfs(x+1,y)
      dfs(x, y+1)
      return True
    return False
    


# 인접 리스트로 구현한 graph일 때의 bfs
# 방문여부를 뜻하는 visited parameter가 별도로 필요하다.

def dfs(graph, vertex, visited):
  # 현재 노드를 방문처리한다.
  visited[vertex] = True
  print(vertex, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문한다.
  for i in graph[vertex]:
    if not visited[i]:
      dfs(graph, i, visited)      

graph = [
	[], # 정점은 1부터 시작하므로 첫 인덱스에 빈 배열 삽입
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5]
    #...
]

 visited = [False] * 9 # vertex의 수
# [False, False, ... ]

dfs(graph, 1, visited)

