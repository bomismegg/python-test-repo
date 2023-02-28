def notInRow(arr, row):

    st = set()

    for i in range(0, 9):
        if arr[row][i] in st:
            return False
        else:
            st.add(arr[row][i])
    return True


def notInCol(arr, col):

    st = set()

    for i in range(0, 9):
        if arr[i][col] in st:
            return False
        else:
            st.add(arr[i][col])
    return True


def notInBox(arr, startRow, startCol):

    st = set()

    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]
            if curr in st:
                return False
            else:
                st.add(curr)
    return True


def isValid(arr, row, col):
    return (notInRow(arr, row) and notInCol(arr, col) and
            notInBox(arr, row - row % 3, col - col % 3))


def isValidConfig(arr, n):

    for i in range(0, n):
        for j in range(0, n):
            if not isValid(arr, i, j):
                return False
    return True

if __name__ == "__main__":

    board = [['2', '6', '7', '4', '3', '1', '8', '5', '9'],
             ['1', '3', '5', '6', '8', '9', '7', '2', '4'],
             ['4', '9', '8', '2', '7', '5', '1', '3', '6'],
             ['9', '8', '1', '7', '5', '2', '6', '4', '3'],
             ['5', '4', '3', '1', '6', '8', '9', '7', '2'],
             ['6', '7', '2', '9', '4', '3', '5', '8', '1'],
             ['7', '2', '6', '8', '1', '4', '3', '9', '5'],
             ['8', '5', '4', '3', '9', '6', '2', '1', '7'],
             ['3', '1', '9', '5', '2', '7', '4', '6', '8']]

    if isValidConfig(board, 9):
        print("YES")
    else:
        print("NO")

    # print("Row")
    # print(notInRow(board,0))
    # print("Col")
    # print(notInCol(board,0))
    # print("Box")
    # print(notInBox(board,0,0))
