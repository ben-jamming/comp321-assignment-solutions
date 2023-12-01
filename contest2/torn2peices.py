def find_path_dfs(s, end, path, table):
    path = path + [s]
    if s == end:
        return path
    
    if s not in table:
        return None
    
    for stop in table[s]:
        if stop not in path:
            new_path = find_path_dfs(stop, end, path, table)
            if new_path:
                return new_path
    return None

        

n = int(input())
table = {} #adjacency matrix
stations = []
for _ in range(n):
    fragments = input().split()
    if fragments[0] not in table:
        table[fragments[0]] = set()
    for node in fragments[1:]:
        if node not in table:
            table[node] = set()
        table[fragments[0]].add(node)
        table[node].add(fragments[0])

table = {node: list(neighbors) for node, neighbors in table.items()}
start, end = input().split()
result = find_path_dfs(start, end, [], table)
if result:
    print(" ".join(result))

else:
    print("no route found")