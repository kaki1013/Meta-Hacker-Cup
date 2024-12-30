f1 = open('cottontail_climb_part_1_input.txt', 'r')
f2 = open('cottontail_climb_part_1_output.txt', 'w')
input = f1.readline
print = f2.write

"""
10^18 : 19 digits
other : 17 digits (odd) = 8 + 1 + 8 (k=8)


"""
def generate_numbers(n):
    k = (n - 1) // 2
    result = []

    for i in range(1, 10 - k):
        inc = ''.join(str(i + j) for j in range(k + 1))
        dec = ''.join(str(i + k - j - 1) for j in range(k))
        num = int(inc + dec)
        result.append(num)

    return result


candidate = []
for length in range(1, 18, 2):
    candidate += generate_numbers(length)

T = int(input())
for test in range(1, T+1):
    A, B, M = map(int, input().split())

    ans = 0
    for c in candidate:
        if A <= c <= B and c % M == 0:
            ans += 1

    print(f"Case #{test}: {ans}\n")

f1.close()
f2.close()