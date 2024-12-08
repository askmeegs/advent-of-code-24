"""
PART ONE 

The computers at the toboggan rental shop are having problems.
Puzzle input is "memory" which is corrupted.  

original goal of the program is to multiply numbers: 
mul(X,Y) where X and Y are between 1-3 digits.  

every other instruction, with other chars, should be ignored. 
for instance, these should be ignored: 

mul(4*, mul(6,9!, ?(12,34)

mul ( 2 , 4 ) 

For this mini example:
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Only these mul instructions are valid: 
mul(2,4), mul(5,5) and mul(11,8) and mul(8,5)

TASK: return the SUM of all the valid mul instructions. 
"""

import re


def count_mul(data):
    results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    s = 0
    for r in results:
        x, y = map(int, r)
        s += x * y
    return s


def part_one():
    with open("input.txt", "r") as f:
        data = f.read()
        data = data.strip()
        print(data)
        results = count_mul(data)
        print("PART 1 SUM: ", results)


"""
PART TWO 

Now we have do and don't instructions added to the mix -- 

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))


You start by doing the mul like part one (mul enabled at start) 
if you hit a don't() turn off mul 
if you hit do() turn back on 

only obey the most RECENT do or don't instruction. 
"""


def part_two_correct():
    with open("input.txt", "r") as f:
        data = f.read().strip()
    data = data.replace("don't()", "\n❌")
    data = data.replace("do()", "\n✅")
    data = "✅" + data  # Start with mul enabled
    data = data.split("\n")

    s = 0
    mul_enabled = True  # Start with mul enabled

    for d in data:
        if d[0] == "❌":
            print("don't")
            mul_enabled = False
        elif d[0] == "✅":
            mul_enabled = True

        if mul_enabled:
            results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", d)
            for r in results:
                x, y = map(int, r)
                s += x * y
    print(s)


"""
This is now correct. The reason this was undercounting was because the input.txt file had newlines, so not all beginning of every line had a marker. so we weren't accounting for continuity (previous marker of do and don't) in thsoe cases.
"""


def part_two_incorrect():
    with open("input.txt", "r") as f:
        data = f.read().strip()
        # remove newlines
        data = data.replace("\n", "")
    data = data.replace("don't()", "\n❌")
    data = data.replace("do()", "\n✅")
    data = "✅" + data  # Start with mul enabled
    data = data.split("\n")

    s = 0

    for d in data:
        print(d)
        if d[0] == "❌":
            print("don't")
        elif d[0] == "✅":
            results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", d)
            for r in results:
                x, y = map(int, r)
                s += x * y
        else:
            print("⚠️ NO MARKER")
    print(s)


if __name__ == "__main__":
    part_two_incorrect()
