"""
나 X 상대 O
가로 N개, 세로 N개 총 2N개만 보면 충분
최소 연산 횟수와 두어야 하는 곳(N-1) set(중복을 피하기 위함, 같은 곳이지만 행과 열에서 모두 체크 되는 경우 방지)
# 취소: 길이가 최대 2N자리 배열에 각 행과 열을 '우승' 조건으로 만들기 위한 최소 연산 횟수 저장
# 단, 불가능한 경우이면 배열에 저장 X
# 빈 리스트이면 불가능, 아니라면 리스트의 최소 원소와 그 개수를 출력
"""


def check(line_list, length):
    if 'O' in set(line_list):
        return [-1]
    return [i for i in range(length) if line_list[i] == '.']


T = int(input())
for test in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    min_operation = N
    operation = set()
    for i in range(N):
        check_row = board[i]
        rowOper = check(check_row, N)
        lenOper = len(rowOper)
        if rowOper != [-1] and lenOper <= min_operation:
            location = tuple(sorted([(i, col) for col in rowOper]))
            if lenOper < min_operation:
                min_operation = lenOper
                operation = set()
            operation.add(location)

        check_column = [board[row][i] for row in range(N)]
        colOper = check(check_column, N)
        lenOper = len(colOper)
        if colOper != [-1] and lenOper <= min_operation:
            location = tuple(sorted([(row, i) for row in colOper]))
            if lenOper < min_operation:
                min_operation = lenOper
                operation = set()
            operation.add(location)

    if operation:
        print(f"Case #{test}: {min_operation} {len(operation)}")
    else:
        print(f"Case #{test}: Impossible")
