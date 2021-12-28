"""
# sol1: 메모리 초과(.이 많은 경우)
우선 X와 O를 모두 가지고 있다면 답은 다음과 같다. (그렇지 않다면 답은 0)
업데이트할 때마다 O에서 X, X에서 O로 바뀌는 최소 구간을 업데이트 함

예를 들어,
1. XOXO라면 index를 기준으로 [(0,1), (1,2), (2, 3), (3, 4)]
2. 업데이트마다 전체 길이(l) 체크하고, '.' 이면 0 <= x < l에 대해 n <= l+x < 2l-1 과 대응됨

업데이트가 끝난 후
위에서 찾은 구간 중 하나를 [a, b]라고 하면 이를 포함하는 substring의 개수를 모두 세면 됨.

0~N-1(index)를 기준으로 a,b를 기록했다면, 그 개수는 (a+1) * (N-b) 이다.

# sol2:
sol1의 기본적인 계산 방법은 유지하되, 정보 처리 방식을 달리 함
예컨대, F...OO.은 FFFFFFFFOOFFFFFFFFOO이 아니라, [19, 'O']로 처리함

그룹을 나눴을 때, 양 끝의 OX와 그룹 끝의 OX를 제외한 모든 정보는 불필요하다.
ex. FFFOFOOXXXFF -> 3 O 2 O 0 X 1 X 2
"""
f1 = open('A3_weak_typing_chapter_3_validation_input - 복사본.txt', 'r')
f2 = open('A3_weak_typing_chapter_3_validation_output - 복사본.txt', 'w')

T = int(f1.readline())
for test in range(1, T+1):
    K = int(f1.readline())
    U = f1.readline()
    mod = 1000000007

    ans = 0
    if 'X' in U and 'O' in U:
        total_length = 0
        first_state, first_idx = 'F', 0
        for i in range(K):
            update = U[i]
            if update == '.':
                total_length *= 2
            else:
                total_length += 1
                if first_state == 'F' and update != 'F':
                    first_state = update
                    first_idx = total_length - 1
        now_length, state, state_idx = first_idx, first_state, first_idx
        sections, sections_length = [], 0

        for i in range(first_idx, K):
            update = U[i]
            if update == '.':
                if state == first_state:
                    state_idx += now_length
                    now_length *= 2
                else:
                    sections.append((state_idx, now_length + first_idx))
                    for section in range(sections_length):
                        a, b = sections[section]
                        if (a, b) == sections[-1]:
                            break
                        sections.append((now_length + a, now_length + b))
                    state_idx += now_length
                    now_length *= 2
                    sections_length += (sections_length + 1)
            else:
                now_length += 1
                if update == 'F':
                    pass
                else:  # 'O', 'X'
                    now_idx = now_length - 1
                    if state == update:
                        state_idx = now_idx
                    else:
                        sections.append((state_idx, now_idx))
                        sections_length += 1
                        state, state_idx = update, now_idx

        ans = 0
        for a, b in sections:
            ans += (a+1) * (total_length-b)
            ans %= mod

    f2.write(f"Case #{test}: {ans}\n")

f1.close()
f2.close()


"""
# f1 = open('A3_weak_typing_chapter_3_validation_input.txt', 'r')
# f2 = open('A3_weak_typing_chapter_3_validation_output.txt', 'w')

# T = int(f1.readline())
T = int(input())
for test in range(1, T+1):
    #K = int(f1.readline())
    #U = f1.readline()
    K, U = int(input()), input()
    mod = 1000000007

    ans = 0
    if 'X' in U and 'O' in U:
        # total_length, first_state, first_idx
        # now_length, state, state_idx
        # sections
        total_length = 0
        first_state, first_idx = 'F', 0
        for i in range(K):
            update = U[i]
            if update == '.':
                total_length *= 2
            else:
                total_length += 1
                if first_state == 'F' and update != 'F':
                    start = i
                    first_state = update
                    first_idx = total_length - 1
        now_length, state, state_idx = first_idx, first_state, first_idx
        sections = []
        print(total_length, first_state, first_idx, now_length, state, state_idx)

        #
        not_need = 0
        for i in range(start, K):
            print(i, not_need, sections)
            update = U[i]
            if update == '.':
                sections.append(state)
                sections.append(not_need)
                temp = 0
                if state == first_state:
                    if sections[-1] not in ['O', 'X']:  # 숫자
                        temp += sections.pop()
                    sections.pop()
                    temp += 1
                    temp += sections.pop()
                    sections.append(temp)
                else:
                    if sections[-1] not in ['O', 'X']:
                        temp += sections.pop()
                    temp += not_need
                    sections.append(temp)
            else:
                now_length += 1
                if update == 'F':
                    not_need += 1
                else:
                    now_idx = now_length - 1
                    if state == update:
                        not_need += 1
                        state_idx = now_idx
                    else:
                        sections.append(not_need)
                        sections.append(state)
                        state = update
                        state_idx = now_idx
                        not_need = 0

        ans = 0
        print(sections, state, state_idx)
#        for a, b in sections:
#            ans += (a+1) * (total_length-b)
#            ans %= mod

#    f2.write(f"Case #{test}: {ans}\n")

#f1.close()
#f2.close()
"""
