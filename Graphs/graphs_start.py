" WE WILL GET STARTED WITH GRAPHS HERE "


# intro to graphs - adjacency marix [drected graph]
def directed():
    
    A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
    maps = []
    
    nodes = 0
    for u, v in A:
        nodes = max(nodes, u, v)
    nodes += 1
    
    
    for _ in range(nodes):
        maps.append([0] * nodes)
        
    for u, v in A:
        maps[u][v] = 1
        
    return maps

# print(directed())




# undirected graph
def undirected():
    
    A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
    res = []
    
    nodes = 0
    for u,v in A:
        nodes = max(nodes, u, v)
    nodes += 1
    
    for _ in range(nodes):
        res.append([0] * nodes)
        
    for u,v in A:
        res[u][v] = 1
        res[v][u] = 1    
        
    return res

# print(undirected())
        
        
        

from collections import defaultdict, deque

# transform into adjacency list
def adjacency_list():
    
    A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
    D = defaultdict(list)
    
    for u,v in A:
        D[u].append(v)
        # D[v].append(u)
        
    return D

# print(adjacency_list())




# DFS Traversals
def dfs_traverse(start):
    
    graph = {0: [1,2], 1: [0,3], 2: [0], 3: [1]}
    seen = set()
    
    def dfs(node):
        seen.add(node)
        for nei in graph[node]:
            if nei not in seen:
                dfs(nei)
                
    dfs(start)
    return seen
            
# print(dfs_traverse(0))



# popping method by BFS
def bfs_traverse(start):
    
    graph = {0: [1,2], 1: [0,3], 2: [0], 3: [1]}
    seen = set([start])
    q = deque([start])
    
    while q:
        node = q.popleft()
        
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                q.append(nei)
    
    return seen

# print(bfs_traverse(0))
    
    
    
    
# popping method by DFS
def dfs_traversal(start):
    
    graph = {0: [1,2], 1: [0,3], 2: [0], 3: [1]}
    seen = set([start])
    res = [start]
    
    while res:
        node = res.pop()
        
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                res.append(nei)
                
    return seen

# print(dfs_traversal(0))





# number of isalnds - [lc - 200]
def num_islands(grid):
    
    if not grid:
        return 0 
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1) 
    
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)
                    
    return islands                 
    
# print(num_islands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]))
    
    
    

# province of city - [lc - 547] 
def province(isConnect):
    
    if not isConnect:
        return 0
    
    n = len(isConnect)
    visited = [False] * n
    isprovince = 0
    
    def dfs(city):
        visited[city] = True
        for nei in range(n):
            if isConnect[city][nei] == 1 and not visited[nei]:
                dfs(nei)
    
    for city in range(n):
        if not visited[city]:
            isprovince += 1
            dfs(city)                   
                   
    return isprovince

# print(province([[1,1,0],[1,1,0],[0,0,1]]))




from collections import deque
# rotting oranges --- [lc - 994]
def rotting_oranges(grid):
    
    if not grid:
        return
    
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    d = deque()
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                d.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
                
                
    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]                
    
    while d and fresh > 0:
        for _ in range(len(d)):
            r, c  = d.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    d.append((nr, nc))
        
        minutes += 1
        
    return minutes if fresh == 0 else -1