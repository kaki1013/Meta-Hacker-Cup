f1 = open('cottontail_climb_part_1_input.txt', 'r')
f2 = open('cottontail_climb_part_1_output.txt', 'w')
# input = f1.readline
# print = f2.write

"""
10^18 : 19 digits
other : 17 digits (odd) = 8 + 1 + 8 (k=8)

we can use 1~8 (middle digit : unique)

"""
def dfs(num, depth, max_depth, increasing, result):
    if depth == max_depth:
        result.append(int(num))
        return

    last_digit = int(num[-1])

    if increasing:
        for next_digit in range(last_digit, 9):
            dfs(num + str(next_digit), depth + 1, max_depth, increasing, result)
    else:
        for next_digit in range(last_digit, 0, -1):
            dfs(num + str(next_digit), depth + 1, max_depth, increasing, result)


def generate_numbers(n):
    k = (n - 1) // 2
    result = []

    for i in range(1, 10 - k):
        increasing_part = str(i)
        temp_result = []
        dfs(increasing_part, 1, k + 1, True, temp_result)

        for num in temp_result:
            decreasing_part = str(num)[-1]
            full_result = []
            dfs(decreasing_part, 1, k + 1, False, full_result)

            for dec_part in full_result:
                full_num = str(num) + str(dec_part)[1:]
                if full_num[k-1] == full_num[k] or full_num[k] == full_num[k+1]:
                    continue
                result.append(int(full_num))

    return result

print(generate_numbers(3))
print(generate_numbers(5))
candidate = []
for length in range(1, 18, 2):
    candidate += generate_numbers(length)
print(len(candidate))
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