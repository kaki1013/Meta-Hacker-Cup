"""
우선 X와 O를 모두 가지고 있다면 답은 다음과 같다. (그렇지 않다면 답은 0)
O에서 X, X에서 O로 바뀌는 최소 구간을 모두 찾음
예를 들어, XOXO라면 index를 기준으로 [(0,1), (1,2), (2, 3), (3, 4)]
위에서 찾은 구간 중 하나를 [a, b]라고 하면 이를 포함하는 substring의 개수를 모두 세면 됨.
0~N-1(index)를 기준으로 a,b를 기록했다면, 그 개수는 (a+1) * (N-b) 이다.
"""
f1 = open('A2_weak_typing_chapter_2_input.txt', 'r')
f2 = open('A2_weak_typing_chapter_2_output.txt', 'w')

T = int(f1.readline())
for test in range(1, T+1):
    N = int(f1.readline())
    S = f1.readline()
    mod = 1000000007
    ans = 0
    if 'X' in S and 'O' in S:
        without_f = [(S[i], i) for i in range(N) if S[i] != 'F']
        sections = []
        state, now = without_f[0][0], without_f[0][1]
        for i in range(len(without_f)):
            check = without_f[i]
            if check[0] != state and check[0] in {'X', 'O'}:
                sections.append((now, check[1]))
                state, now = check[0], check[1]
            if check[0] == state and check[0] in {'X', 'O'}:
                now = check[1]
        for a, b in sections:
            ans += (a+1)*(N-b)
            ans %= mod
    f2.write(f"Case #{test}: {ans}\n")

f1.close()
f2.close()