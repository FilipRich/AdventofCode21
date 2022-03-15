my_file = open("day2/input-day2.txt", "r")
mylist = my_file.read().split("\n")

def part1():
    horizontal_pos = 0
    depth = 0
    for i in mylist:
        if "forward" in i:
            for x in i:
                if x.isdigit():
                    horizontal_pos += int(x)
        elif "down" in i:
            for x in i:
                if x.isdigit():
                    depth += int(x)
        elif "up" in i:
            for x in i:
                if x.isdigit():
                    depth -= int(x)

    print(horizontal_pos * depth)

def part2():
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in mylist:
        if "forward" in i:
            for x in i:
                if x.isdigit():
                    horizontal_pos += int(x)
                    depth += (int(x)*aim)
        elif "down" in i:
            for x in i:
                if x.isdigit():
                    aim += int(x)
        elif "up" in i:
            for x in i:
                if x.isdigit():
                    aim -= int(x)
        
    print(horizontal_pos * depth)

part1()
part2()