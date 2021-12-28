"""
"""
f1 = open('A1_weak_typing_chapter_1_input.txt', 'r')
f2 = open('A1_weak_typing_chapter_1_ouput.txt', 'w')

T = int(f1.readline())
for test in range(1, T+1):
    N = int(f1.readline())
    W = f1.readline()
    without_f = [W[i] for i in range(N) if W[i] != 'F']
    ans = 0
    l = len(without_f)
    for i in range(l-1):
        if without_f[i] != without_f[i+1]:
            ans += 1
    f2.write(f"Case #{test}: {ans}\n")
f1.close()
f2.close()