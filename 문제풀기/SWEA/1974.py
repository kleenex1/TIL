import sys

sys.stdin = open("_스도쿠검증.txt", "r")

T = int(input())
def sudo(sudoku):
    for i in range(9):
        sudo = []
        for j in range(9):
            if sudo:
                if sudoku[i][j] in sudo:
                    return '0'
            sudo.append(sudoku[i][j])
    for i in range(9):
        sudo = []
        for j in range(9):
            if sudo:
                if sudoku[j][i] in sudo:
                    return '0'
            sudo.append(sudoku[j][i])

    for k in range(0,9,3):
        for r in range(0, 9, 3):
            sudo = []
            for t in range(3):
                for o in range(3):
                    if sudo:
                        if sudoku[k+t][r+o] in sudo:
                            return '0'
                    sudo.append(sudoku[k+t][r+o])
 
    return '1'

for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(1, 9 + 1)]
    print("#{}".format(test_case), end=' ')
    print(sudo(sudoku))
 