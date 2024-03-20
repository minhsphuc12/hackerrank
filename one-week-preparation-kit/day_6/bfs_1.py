# graph = {'A': ['B', 'C'],
#              'B': ['C', 'E'],
#              'C': ['D'],
#              'D': ['C'],
#              'E': ['F'],
#              'F': ['C'],
#              'G': ['H'],
#              'H': []}

# def bfs(g, start_node):
#     visited = [start_node]
#     to_visit = g[start_node].copy()
#     print('visited', visited, 'to_visit', to_visit)
#     while len(to_visit) > 0: 
#         current_node = to_visit.pop(0)
#         visited.append(current_node)
#         to_visit = to_visit + [node for node in g[current_node] if node not in visited and node not in to_visit]
#         print('visited', visited, 'to_visit', to_visit)
#     return visited

# bfs(graph, 'A')

# pairs = [['A', 'B'], ['A', 'C'], ['B', 'C'], ['B', 'E'], ['C', 'D'],['D', 'C'],['E', 'F'],['F', 'E'], ['G', 'H']]
# def convert_edge_list_to_adjacent_list(pairs):
#     nodes = sorted(set([x for pair in pairs for x in pair]))
#     adjacent_list = {node:[] for node in nodes}
#     for pair in pairs:
#         adjacent_list[pair[0]].append(pair[1])
#         adjacent_list[pair[1]].append(pair[0])
#     adjacent_list = {k:sorted(set(v)) for k,v in adjacent_list.items()}
#     return adjacent_list


# def bfs_2(g, start_node):
#     step = 0
#     visited = {start_node: step}
#     to_visit = g[start_node].copy()
#     print('visited', visited, 'to_visit', to_visit)
#     while len(to_visit) > 0: 
#         current_node = to_visit.pop(0)
#         step += 1
#         visited[current_node] = step
#         to_visit = to_visit + [node for node in g[current_node] if node not in visited and node not in to_visit]
#         print('visited', visited, 'to_visit', to_visit)
#     nodes = sorted(list(graph.keys()))
#     output = {node:visited[node]*6 if node in visited else -1 for node in nodes}
#     return output

# bfs_2(graph, 'A')

def bfs_3(n, m , edges, s):
    # n = 9
    nodes = list(range(1,n+1))
    def convert_edge_list_to_adjacent_list(edge_list, nodes):
        # nodes = sorted(set([x for pair in edge_list for x in pair]))
        adjacent_list = {node:[] for node in nodes}
        for pair in edge_list:
            adjacent_list[pair[0]].append(pair[1])
            adjacent_list[pair[1]].append(pair[0])
        adjacent_list = {k:sorted(set(v)) for k,v in adjacent_list.items()}
        return adjacent_list
    
    adj_list = convert_edge_list_to_adjacent_list(edges, nodes)

    def bfs_2(adj_list, start_node, nodes):
        step = 0
        visited = {start_node: step}
        to_visit:list = adj_list[start_node].copy()
        next_visit = []
        # print('visited', visited, 'to_visit', to_visit)
        stop = len(to_visit) == 0 and len(next_visit) == 0
        while not stop:
            step += 1
            while len(to_visit) > 0: 
                current_node = to_visit.pop(0)
                visited[current_node] = step
                next_visit = next_visit + [node for node in adj_list[current_node] if node not in visited and node not in to_visit]
                # print('visited', visited, 'to_visit', to_visit, 'next_visit', next_visit)
            to_visit = next_visit
            stop = len(to_visit) == 0 and len(next_visit) == 0
        output = {node:visited[node]*6 if node in visited else -1 for node in nodes}
        return output
    visited_dict = bfs_2(adj_list=adj_list, start_node=s, nodes=nodes)
    visited_dict
    return list({k:v for k,v in visited_dict.items() if k!=s}.values())

def bfs_3(n, m , edges, s):
    from collections import deque
    # Convert edge list to adjacency list
    def convert_edge_list_to_adjacent_list(edge_list, nodes):
        adjacent_list = {node: [] for node in nodes}
        for u, v in edge_list:
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)
        return adjacent_list
    
    adj_list = convert_edge_list_to_adjacent_list(edges, list(range(1, n + 1)))
    
    # Perform BFS
    def bfs_2(adj_list, start_node, nodes):
        visited = {node: -1 for node in nodes}  # Track visited nodes and distances
        queue = deque([(start_node, 0)])  # Use deque for efficient pops from the front
        visited[start_node] = 0
        
        while queue:
            current_node, step = queue.popleft()  # Efficiently remove the leftmost item
            for neighbor in adj_list[current_node]:
                if visited[neighbor] == -1:  # If not visited
                    visited[neighbor] = step + 6  # Update distance
                    queue.append((neighbor, step + 6))  # Enqueue neighbor
        
        return [visited[node] for node in nodes if node != start_node]
    
    return bfs_2(adj_list=adj_list, start_node=s, nodes=list(range(1, n + 1)))


# pairs = [[1,2], [1,3], [2,3], [2,5], [3,4]]
# bfs_3(8, 5, pairs, 1)
bfs_3(n=4,m=3, edges=[[4,2], [1,2], [2,3]], s=2)
bfs_3(n=5,m=3, edges=[[4,2], [1,2], [2,3]], s=2)
n=4;m=3; edges=[[4,2], [1,2], [2,3]]; s=2; start_node=s

def dfs(g, start_node):
    visited = [start_node]
    to_visit:list = g[start_node].copy()
    print('visited', visited, 'to_visit', to_visit)
    while len(to_visit) > 0: 
        current_node = to_visit.pop(0)
        visited.append(current_node)
        to_visit = [node for node in g[current_node] if node not in visited and node not in to_visit] + to_visit
        print('visited', visited, 'to_visit', to_visit)
    return visited

# dfs(graph, 'A')