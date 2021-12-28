from collections import deque


def movable(aa, bb, edge, adjj):
    visited = [False] * (N+1)
    q = deque([aa])
    visited[aa] = True
    while q:
        print(q)
        now = q.popleft()
        visited[now] = True
        for nxt in adjj[now]:
            if {now, nxt} == set(edge):
                continue
            if not visited[nxt]:
                q.append(nxt)
            if nxt == bb:
                return True
    return False


def protectable(s, e, groupp, adjj):
    for k in groupp:
        kk = groupp[k]
        if len(kk) == 1:
            continue
        for a in kk:
            for b in kk:
                if a != b and not movable(a, b, (s, e), adjj):
                    return True
    return False


T = int(input())
for test in range(1, T+1):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    adj = [[] for _ in range(N+1)]
    for a, b in AB:
        adj[a].append(b)
        adj[b].append(a)
    F = list(map(int, input().split()))
    group = dict()
    for i in range(N):
        if F[i] in group:
            group[F[i]].append(i+1)
        else:
            group[F[i]] = [i+1]
    ans = N - 1
    for a, b in AB:
        print(a, b)
        if protectable(a, b, group, adj):
            ans -= 1
    print(f"Case #{test}: {ans}")

