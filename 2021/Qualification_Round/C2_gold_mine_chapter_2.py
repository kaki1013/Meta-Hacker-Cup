"""
0. 가능한 경우는
(1) (1~a) + (b~c) + .. + (x~y) + (z~1)
(2) (1~a) + (b~c) + .. + (y~z) + 1
1. 간선 이용 시, 간선의 양 끝 노드의 인접리스트에서 해당 간선의 정보를 삭제
2. 그렇다면 어떤 간선을 이용해야 하는가? 포인트는 '트리의 지름'
(1) 처음에 1번에서 시작할 때: 1에서 가장 먼 곳으로 이동(여러 개일 경우, 시작하면서 가는 곳의 아닌 곳으로 )
(2)
"""


# 입력 받은 노드를 기준으로
# '입력 받은 노드의 C 값' + '입력 노드와 인접한 자식 노드(1번 제외 = index 0번 제외)로부터, 리프 노드까지의 경로에 존재하는 노드들의 C 값의 합으로 가는한 값 중 최대인 값을 반환
def max_route_sum(node, graph, value, parent):
    if len(graph[node]) == 1:  # 리프노드(base condition)
        return value[node]
    max_sum = value[node]
    child_route_sum = []
    for child in graph[node]:
        if child == 0 or child == parent:
            continue
        child_route_sum.append(max_route_sum(child, graph, value, node))
    max_sum += max(child_route_sum)
    return max_sum


T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    max_collectable = sum(C)
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        adj[A-1].append(B-1)
        adj[B-1].append(A-1)

    ans = C[0]
    if N != 1:
        while K != 0:
            if ans == max_collectable:
                break
            if K == 1:
                if not len(adj[0]):
                    ans += max_route_sum(adj[0][0], adj, C, -1)
                else:
                    sums = sorted([max_route_sum(child, adj, C, -1) for child in adj[0]])
                    ans += (sums[-1] + sums[-2])
            else:  # K > 1
                pass
            K -= 1

    print(f"Case #{test}: {ans}")

"""
50--
9 2
2 14 7 6 11 3 6 1 8
4 5
6 7
8 9
1 3
6 8
2 4
4 1
1 8
"""
