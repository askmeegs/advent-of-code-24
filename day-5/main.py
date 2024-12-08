"""
PART ONE 

Next stop - book stacks in a basement.
Problem - sleigh launch safety manual updates won't print. 
The input has two parts.
The first part is format X|Y - means that if page X and Y must 
both be printed in the update, X must appear at some point before Y.

The second set of input is the pages we must produce FOR EACH update.  
In the input below, we are maxing SIX updates to the manual. 

RULES:  {'47': ['53', '13', '61', '29'], '97': ['13', '61', '47', '29', '53', '75'], '75': ['29', '53', '47', '61', '13'], '61': ['13', '53', '29'], '29': ['13'], '53': ['29', '13']}

47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47


TASK: identify which updates are in the right order based on the rules. 
If the page IS correctly ordered, return the MIDDLE number. 
The final result should be the sum of all middle numbers. 

Answer to input mini is 143. 
"""


def is_ordered(r_dict, u):
    # print("\n\n🤔 checking if ", u, " is ordered")
    for i in range(0, len(u)):
        x = u[i]
        # print("checking ", x)
        if x in r_dict:
            j = i - 1
            while j >= 0:
                # print(j)
                if u[j] in r_dict[x]:
                    # print("⚠️ not ordered: ", u[j], " must come before ", x)
                    return False
                j -= 1
        else:
            # print("NO RULES FOR ", x)
            continue
    # print("✅ yes, ordered: ", u)
    return True


# brute force, to start ...
def part_one():
    with open("input.txt") as f:
        data = f.read()
    data = data.split("\n\n")
    rules = data[0]
    rules = rules.split("\n")
    rules = [rule.split("|") for rule in rules]
    r_dict = {}
    for r in rules:
        i = r[0]
        j = r[1]
        if i not in r_dict:
            r_dict[i] = [j]
        else:
            r_dict[i].append(j)

    print("RULES: ", r_dict)
    updates = data[1]
    updates = updates.split("\n")
    updates = [update.split(",") for update in updates]
    print("UPDATES: ", updates)

    # our r_dict is the rules stated as: key k must come before all the values in v
    # sum of middles for correctly-ordered updates
    result = 0
    for u in updates:
        if is_ordered(r_dict, u):
            mid = int(u[len(u) // 2])
            print(mid)
            result += mid
    print("🏁 RESULT: ", result)


"""
PART TWO 

"""


def reorder(r_dict, u):
    for i in range(0, len(u)):
        x = u[i]
        if x in r_dict:
            j = i - 1
            while j >= 0:
                if u[j] in r_dict[x]:
                    u[i], u[j] = u[j], u[i]
                    break
                j -= 1
    return u


def part_two():
    with open("input.txt") as f:
        data = f.read()
    data = data.split("\n\n")
    rules = data[0]
    rules = rules.split("\n")
    rules = [rule.split("|") for rule in rules]
    r_dict = {}
    for r in rules:
        i = r[0]
        j = r[1]
        if i not in r_dict:
            r_dict[i] = [j]
        else:
            r_dict[i].append(j)

    print("RULES: ", r_dict)
    updates = data[1]
    updates = updates.split("\n")
    updates = [update.split(",") for update in updates]
    print("UPDATES: ", updates)

    result = 0
    for u in updates:
        print("\n🕰️ checking: ", u)
        if not is_ordered(r_dict, u):
            numt = 1
            rev = reorder(r_dict, u)
            while not is_ordered(r_dict, rev):
                rev = reorder(r_dict, rev)
                numt += 1
            print("🌪️ I reordered {} times to get {}".format(numt, rev))
            mid = int(rev[len(rev) // 2])
            print(mid)
            result += mid
        else:
            print("✅ this one is ordered, ignoring.")
    print("🏁 RESULT: ", result)


if __name__ == "__main__":
    # part_one()
    part_two()
