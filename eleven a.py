n = int(input("Enter the number of users: "))
matrix = [[0 for _ in range(n)] for _ in range(n)]

m = int(input("Enter the number of connections: "))

print("Enter the connections (u v):")
for i in range(m):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

print("\nAdjacency Matrix:")
for row in matrix:
    print(*row)

adj_list = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            adj_list[i].append(j)

print("\nAdjacency List:")
for i in range(n):
    print(i, "->", adj_list[i])

u, v = map(int, input("\nEnter two users to check connection: ").split())

if matrix[u][v] == 1:
    print("Users are directly connected.")
else:
    print("Users are not directly connected.")
