from collections import deque


def movable(aa, bb, edge, adjj):
    visited = [False] * (N+1)
    q = deque([aa])
    visited[aa] = True
    while q:
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
                if not movable(a, b, (s, e), adjj):
                    return True
    return False


f1 = open('B_chainblock_validation_input.txt', 'r')
f2 = open('B_chainblock_validation_output.txt', 'w')

T = int(f1.readline())
for test in range(1, T+1):
    N = int(f1.readline())
    AB = [list(map(int, f1.readline().split())) for _ in range(N-1)]
    adj = [[] for _ in range(N+1)]
    for a, b in AB:
        adj[a].append(b)
        adj[b].append(a)
    F = list(map(int, f1.readline().split()))
    group = dict()
    for i in range(N):
        if F[i] in group:
            group[F[i]].append(i+1)
        else:
            group[F[i]] = [i+1]
    ans = N - 1
    for a, b in AB:
        if protectable(a, b, group, adj):
            ans -= 1
    f2.write(f"Case #{test}: {ans}\n")

f1.close()
f2.close()
