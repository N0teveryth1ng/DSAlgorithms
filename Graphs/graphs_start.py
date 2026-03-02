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





