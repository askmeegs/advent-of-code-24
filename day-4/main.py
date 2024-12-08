"""
PART ONE 

Word search 


MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

TASK - find all instances of XMAS 
words can be: horizontal, vertical, diagonal, written backwards, or even overlapping other words 

Here XMAS occurs 18 times: 

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""


def word_search(data, word):
    r = 0
    n = len(data)

    # Horizontal and vertical
    for i in range(n):
        for j in range(n - len(word) + 1):
            if word in "".join(data[i][j : j + len(word)]):
                r += 1
            if word in "".join([data[j + k][i] for k in range(len(word))]):
                r += 1

    # Diagonal (top-left to bottom-right)
    for i in range(n - len(word) + 1):
        for j in range(n - len(word) + 1):
            if word in "".join([data[i + k][j + k] for k in range(len(word))]):
                r += 1

    # Diagonal (top-right to bottom-left)
    for i in range(n - len(word) + 1):
        for j in range(len(word) - 1, n):
            if word in "".join([data[i + k][j - k] for k in range(len(word))]):
                r += 1

    return r


def part_one():
    with open("input.txt") as f:
        data = f.read().splitlines()
    final_result = word_search(data, "XMAS")
    final_result += word_search(data, "SAMX")
    print("OCCURRENCES :", final_result)


"""
PART TWO 

Now instead of searching for XMAS or SAMX, we're looking for a "MAS" in an X formation

M.S
.A.
M.S

Where A is the "hub" 

The MAS can be written forwards or backwards - and it can be different within an MAS formation. 

Count the total number of X-MAS formations in the grid.
"""


def part_two():
    return


if __name__ == "__main__":
    # part_one()
    part_two()
