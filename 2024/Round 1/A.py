f1 = open('A_subsonic_subway_input.txt', 'r')
f2 = open('A_subsonic_subway_output.txt', 'w')

e = 1e-100

input = f1.readline
print = f2.write
T = int(input())
for test in range(1, T+1):
    N = int(input())

    mm, MM = [], []
    for i in range(1, N+1):
        A, B = map(int, input().split())

        if A == 0:
            M = i / (A+e)
        else:
            M = i / A

        if B == 0:
            m = i / (B+e)
        else:
            m = i / B

        mm.append(m)
        MM.append(M)

    ans = max(mm) if max(mm) <= min(MM) else -1
    ans = round(ans, 10)

    print(f"Case #{test}: {ans}\n")

f1.close()
f2.close()