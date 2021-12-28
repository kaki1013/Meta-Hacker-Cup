"""
sol1 -> TLE
bfs로 순회, ans = -1로 초기화
인접은 K개, visited는 문자열 set, 시작은 주어진 (문자열, 0), q가 비거나 한 문자 문자열을 찾을 때까지
코드
from collections import deque
T = int(input())
for test in range(1, T+1):
    ans = -1
    S, K = input(), int(input())
    l = len(S)
    replacements = [input() for _ in range(K)]
    visited = {S}
    q = deque([(S, 0)])
    while q:
        now, dist = q.popleft()
        if len(set(now)) == 1:
            ans = dist
            break
        for replacement in replacements:
            before, after = replacement[0], replacement[1]
            for i in range(l):
                if now[i] == before:
                    candidate = now[:i] + after + now[i+1:]
                    if candidate not in visited:
                        q.append((candidate, dist+1))
                        visited.add(candidate)
    print(f"Case #{test}: {ans}")

sol2
K와 플로이드 와샬로 A~Z -> A~Z 최단거리 모두 구하고 (26*26), 단 불가능한 경우 잘 체크할 것
가능한 경우(만들어질 수 있고, 한 문자 문자열, 예컨대 AAA...A ~ ZZZ... ZZ)만 판단
예를 들어, ABCD..XYZ -> UUUU...UUU
A -> U, B -> U 를 하고 연산 횟수를 더함
불가능하면 더하지 않고 -1 출력 후 다음 경우를 탐색
"""
T = int(input())
for test in range(1, T+1):
    ans = 10 ** 5
    S, K = input(), int(input())
    l = len(S)
    dist = [[100 for _ in range(26)] for _ in range(26)]
    for _ in range(K):
        start, end = map(ord, list(input()))
        start -= 65
        end -= 65
        dist[start][end] = 1

    # floyd-warshall
    for i in range(26):
        dist[i][i] = 0
    for k in range(26):
        for i in range(26):
            for j in range(26):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(26):
        for j in range(26):
            if dist[i][j] == 100:
                dist[i][j] = 0
    for i in range(26):
        dist[i][i] = -1

    # AA..A ~ ZZ..Z
    for goal in range(26):
        seconds = 0
        broken = False
        for i in range(l):
            char = ord(S[i]) - 65
            if dist[char][goal] == -1:
                continue
            if dist[char][goal] == 0:
                broken = True
                break
            else:
                seconds += dist[char][goal]
        if broken:
            continue
        ans = min(ans, seconds)

    print(f"Case #{test}: {ans if ans != 10**5 else -1}")
