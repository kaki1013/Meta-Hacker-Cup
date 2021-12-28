f1 = open('B_traffic_control_input.txt', 'r')
f2 = open('B_traffic_control_output.txt', 'w')

T = int(f1.readline())
for test in range(1, T+1):
    N, M = map(int, f1.readline().split())
    S = list(map(int, f1.readline().split()))
    P = [list(map(int, f1.readline().split())) for _ in range(N)]
    ans = 0

    f2.write(f"Case #{test}: {ans}\n")

f1.close()
f2.close()