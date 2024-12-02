"""
PART ONE 

The first search location is a nuclear plant. 
They are dealing with unusual data.  
Each report= 1 line.  
Each character in the report (line) has X "levels" 

Task - figure out which reports (lines) are SAFE 

A safe report must have items all increasing or decreasing 
AND 
Any two adjacent levels must differ by between 1 and 3 (inclusive) 

Return the TOTAL NUMBER of SAFE LEVELS 
"""


def is_safe(report):
    # print("\n🕰️ Checking report: ", report)
    # check sorted condition
    if report != sorted(report) and report != sorted(report, reverse=True):
        # print("Failed sorted condition")
        return False
    # check difference condition
    for i in range(0, len(report) - 1):
        if abs(report[i + 1] - report[i]) < 1 or abs(report[i + 1] - report[i]) > 3:
            # print("Failed difference condition")
            return False
    # print("Report is safe")
    return True


def check_remove(report):
    for i in range(0, len(report)):
        temp = report.copy()
        temp.pop(i)
        if is_safe(temp):
            print(
                "⚠️ Report {} is safe after removing element {}".format(
                    report, report[i]
                )
            )
            return True
    return False


def part_one():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
        data = [line.split() for line in data]
        for i in range(0, len(data)):
            temp = []
            for j in range(0, len(data[i])):
                temp.append(int(data[i][j]))
            data[i] = temp
        safe = 0
        for i in range(0, len(data)):
            if is_safe(data[i]):
                safe += 1
        print("Total number of safe reports: ", safe)


def part_one():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
        data = [line.spl it() for line in data]
        for i in range(0, len(data)):
            temp = []
            for j in range(0, len(data[i])):
                temp.append(int(data[i][j]))
            data[i] = temp
        safe = 0
        for i in range(0, len(data)):
            if is_safe(data[i]):
                print("✅ Report {} is safe already".format(i + 1))
                safe += 1
            elif check_remove(data[i]):
                safe += 1
            else:
                print(
                    "❌ Report {} is not safe after checking all remove".format(i + 1)
                )
        print("Total number of safe reports: ", safe)


if __name__ == "__main__":
    part_one()
