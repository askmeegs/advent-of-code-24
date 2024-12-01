"""
- Chief Historian is missing. 
- Look for him at historically significant locations. 
- Will look at 50 places total, two per day before 12/25  
- First task is to populate the list of locations.  
- a group of historians scours the office and assembles two separate lists of location IDs, but they're different.  

3   4
4   3
2   5
1   3
3   9
3   3


PART ONE TASK: 
- pair up the smallest number in the left list with the smallest in the right list, then keep going. 
- within each pair, get the diff.  
- then ADD UP 

"""


def read_input(file_path: str) -> tuple:
    with open(file_path, "r") as file:
        data = file.readlines()
        data = [line.strip().split() for line in data]
        left_list = [int(line[0]) for line in data]
        right_list = [int(line[1]) for line in data]
    return left_list, right_list


def part_one():
    left_list, right_list = read_input("input.txt")
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    result = 0
    for i in range(0, len(left_list)):
        result += abs(left_list[i] - right_list[i])
    print("RESULT: ", result)


"""
How often does each number from the left list appear in the right list? 

"""


def part_two():
    left_list, right_list = read_input("input.txt")
    occur = {}
    for i in left_list:
        occur[i] = 0
    for i in right_list:
        if i in occur:
            occur[i] += 1
    result = 0
    for i in left_list:
        result += i * occur[i]
    print("RESULT: ", result)


if __name__ == "__main__":
    part_two()
