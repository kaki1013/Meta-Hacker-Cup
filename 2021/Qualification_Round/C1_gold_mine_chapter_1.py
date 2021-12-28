"""
ans = 1번 노드 값
N이 1이라면 여기서 종료, 아니라면 다음과 같이 두 가지 경우로 분류
1번 노드의 자식 노드가 하나라면, '해당 노드부터 리프 노드까지의 경로들' 중 '경로 위의 노드의 값들의 합이 최대가 될 때 그 합'을 ans에 더함
그렇지 않다면, 자식 노드들에 대해 위의 '합'들을 구하여 최대인 값과 두 번째로 큰 값을 ans에 더함

why?
1. 우선 자식 노드로 가고 나면, 트리이기 때문에(지나온 노드로 다시 갈 수 없음) '중간에 1번으로 가는 것'보다 '리프 노드까지 가는 것'이 이득 (처음에는 반드시 리프 노드까지 이동)
2. 리프 노드 이후에는 '1번 노드로 가는 것'과 '나머지 노드로 가는 것'의 2가지 선택지가 존재
3. 이때 나머지 노드로 가는 선택지를 고르기 위해서는, 나머지 노드로 이동했을 때 1번 노드로 가는 경로가 존재해야 함
4. 즉, 2번에서 '1번 노드로 이동'은 1번 노드(루트 노드)의 자식 노드가 1개일 때만 선택해야 하며,
    자식 노드가 2개 이상이라면 루트의 자식 노드 중 처음 고른 것이 아닌 나머지 자식 노드로 가는 리프 노드로 이동하여 르프에서 1번으로 이동해야 함
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
    N = int(input())
    C = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        adj[A-1].append(B-1)
        adj[B-1].append(A-1)

    ans = C[0]
    if N != 1:
        if len(adj[0]) == 1:
            ans += max_route_sum(adj[0][0], adj, C, -1)
        else:
            sums = sorted([max_route_sum(child, adj, C, -1) for child in adj[0]])
            ans += (sums[-1] + sums[-2])

    print(f"Case #{test}: {ans}")
