# Q1
# N = int(input())
# S = input().strip()

# count_A, count_B, count_C = 0, 0, 0

# min_position = N

# for i in range(N):
#     if S[i] == 'A':
#         count_A += 1

#     elif S[i] == 'B':
#         count_B += 1

#     elif S[i] == 'C':
#         count_C += 1

#     if count_A >= 1 and count_B >= 1 and count_C >= 1:
#         min_position = i+1
#         break

# print(min_position)


# Q2
# N, D = map(int, input().split())

# schedule = [input().strip() for _ in range(N)]


# max_idle_days = 0
# idle_days = 0
# for i in range(D):
#     all_o = True
#     for j in range(N):
#         if schedule[j][i] != 'o':
#             all_o = False
#             break

#     if all_o:
#         idle_days += 1
    
#     else:
#         idle_days = 0

#     max_idle_days = max(max_idle_days, idle_days)


# print(max_idle_days)

# Q3
# def find_cycle(graph, start, visited, cycle):
#     visited[start] = True
#     cycle.append(start)

#     next_node = graph[start]
#     if not visited[next_node]:
#         find_cycle(graph, next_node, visited, cycle)
#     else:
#         # 既に訪れた頂点を再度訪れた場合、有向閉路が見つかったとして探索終了
#         cycle.append(next_node)
#         return True

#     return False  # ここでFalseを返す

# def find_directed_cycle(N, graph):
#     visited = [False] * (N + 1)
#     for i in range(1, N + 1):
#         if not visited[i]:
#             cycle = []
#             if find_cycle(graph, i, visited, cycle):
#                 return cycle

# # 入力を受け取る
# N = int(input())
# A = list(map(int, input().split()))

# # インデックスを1-originにするためにダミーノードを追加
# graph = [0] + A

# # 結果を出力
# result = find_directed_cycle(N, graph)
# print(len(result))
# print(*result)
N = int(input())




# Q4




