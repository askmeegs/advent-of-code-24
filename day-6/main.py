"""
PART ONE 

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

^ is the guard facing up 
TASK: count the number of distinct locations visited before the guard crosses the boundaries of the map ("leaves the area") and mark as visited with X 

Rules of movement: 
- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.
"""


def pp(M):
    print("\n------------------------------ ")
    for row in M:
        print(row)
    print("------------------------------\n")


def part_one():
    with open("input.txt") as f:
        M = f.read().splitlines()
    rows = len(M)
    cols = len(M[0])
    g_r = 0
    g_c = 0
    for i in range(rows):
        for j in range(cols):
            if M[i][j] == "^":
                g_r = i
                g_c = j
                break
    print("guard starts at  ", g_r, g_c)

    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

    # v is num locations visited
    v = 1
    pos = M[g_r][g_c]
    temp = list(M[g_r])
    temp[g_c] = "X"
    M[g_r] = "".join(temp)

    # while guard is in the boundaries of the map ...
    while True:
        print("\n\n⭐ location # ", v, "guard is at: ", g_r, g_c, " facing ", pos)
        pp(M)
        if pos == UP:
            if g_r - 1 < 0:
                print("🏁 guard exited the map")
                break
            if M[g_r - 1][g_c] == "#":
                pos = RIGHT
            else:
                g_r -= 1
                if M[g_r][g_c] != "X":
                    v += 1
                    temp = list(M[g_r])
                    temp[g_c] = "X"
                    M[g_r] = "".join(temp)
        elif pos == DOWN:
            if g_r + 1 >= rows:
                print("🏁 guard exited the map")
                break
            if M[g_r + 1][g_c] == "#":
                pos = LEFT
            else:
                g_r += 1
                if M[g_r][g_c] != "X":
                    v += 1
                    temp = list(M[g_r])
                    temp[g_c] = "X"
                    M[g_r] = "".join(temp)
        elif pos == LEFT:
            if g_c - 1 < 0:
                print("🏁 guard exited the map")
                break
            if M[g_r][g_c - 1] == "#":
                pos = UP
            else:
                g_c -= 1
                if M[g_r][g_c] != "X":
                    v += 1
                    temp = list(M[g_r])
                    temp[g_c] = "X"
                    M[g_r] = "".join(temp)
        elif pos == RIGHT:
            if g_c + 1 >= cols:
                print("🏁 guard exited the map")
                break
            if M[g_r][g_c + 1] == "#":
                pos = DOWN
            else:
                g_c += 1
                if M[g_r][g_c] != "X":
                    v += 1
                    temp = list(M[g_r])
                    temp[g_c] = "X"
                    M[g_r] = "".join(temp)

    pp(M)
    print("✅ visited ", v, " locations")


"""
PART TWO 

"""


def part_two():
    return


if __name__ == "__main__":
    part_one()
    # part_two()
