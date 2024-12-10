"""
PART ONE 

There's a broken rope bridge. 
The input is a series of equations.  

190: 10 19 

TEST_VALUE: OPERAND OPERAND .. 
You can ONLY add or multiply. 

190 = 10 * 19 


3267: 81 40 27
81 + 40 * 27 OR 81 * 40 + 27

NOTE - evaluate left to right, ignore order of operations. 

MUST RETURN: the sum of the test values with valid equations. 
"""


# 0 is +
# 1 is *
def gen_perms_part_one():
    perms = {}
    for i in range(1, 13):
        temp = []
        # temp is all the possible combinations of * and + operands for a string of length i
        # bin() is a binary string of that number
        for j in range(2 ** (i - 1)):
            temp.append(bin(j)[2:].zfill(i - 1))
        perms[i - 1] = temp
    return perms


def part_one():
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = [x.strip() for x in data]
    D = {}
    max_operands_len = 1
    for d in data:
        d = d.split(":")
        test_value = int(d[0])
        operands = d[1].strip()
        operands = d[1].split()
        operands = [int(x) for x in operands]
        if len(operands) > max_operands_len:
            max_operands_len = len(operands)
        D[test_value] = operands
    # print(D)
    print("max operands length: ", max_operands_len)

    perms = gen_perms_part_one()
    result = 0
    # [6, 8, 6, 15] perms:  ['000', '001', '010', '011', '100', '101', '110', '111']
    for output, operands in D.items():
        pp = perms[len(operands) - 1]
        # print(
        #     "\n\n evaluating output: ",
        #     output,
        #     "operands: ",
        #     operands,
        #     "with pp: ",
        #     perms,
        # )
        for p in pp:
            # print(p)
            i = 0
            temp = operands[i]
            while i < len(operands) - 1:
                if p[i] == "0":
                    temp = temp + operands[i + 1]
                else:
                    temp = temp * operands[i + 1]
                i += 1
            if temp == output:
                result += output
                break
    print("PART 1 SUM: ", result)


"""
PART TWO 

adds || (string concat) operator 
"""


# NOTE: github copilot helped me debug this helper function
def base3(n):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return "".join(digits[::-1])


# 0 is +
# 1 is *
# 2 is || (concat)
def gen_perms_part_two():
    perms = {}
    for i in range(1, 13):
        temp = []
        for j in range(3 ** (i - 1)):
            temp.append(base3(j).zfill(i - 1))
        perms[i - 1] = temp
    return perms


def part_two():
    perms = gen_perms_part_two()
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = [x.strip() for x in data]
    D = {}
    max_operands_len = 1
    for d in data:
        d = d.split(":")
        test_value = int(d[0])
        operands = d[1].strip()
        operands = d[1].split()
        operands = [int(x) for x in operands]
        if len(operands) > max_operands_len:
            max_operands_len = len(operands)
        D[test_value] = operands

    perms = gen_perms_part_two()
    result = 0
    for output, operands in D.items():
        print("output: ", output, "operands: ", operands)
        pp = perms[len(operands) - 1]
        for p in pp:
            i = 0
            temp = operands[i]
            while i < len(operands) - 1:
                if p[i] == "0":
                    temp = temp + operands[i + 1]
                elif p[i] == "1":
                    temp = temp * operands[i + 1]
                else:
                    temp = str(temp) + str(operands[i + 1])
                    temp = int(temp)
                i += 1
            if temp == output:
                result += output
                break
    print("PART 1 SUM: ", result)


if __name__ == "__main__":
    # part_one()
    part_two()
