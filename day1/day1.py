class FileHandler:
    def __init__(self, file) -> None:
        self.file = file


    def read_file(self):
        my_file = open(self.file, "r")
        return my_file.read()


def part1(): #this function answers part 1
    file = FileHandler("day1/input-day1.txt")
    my_file = file.read_file()
    new_file = my_file.split("\n")

    counter = 0
    for i,x in enumerate(new_file):
        if i == 0:
            pass
        else:
            pre = new_file[i-1]
            if int(x) > int(pre):
                counter += 1
        
    print(counter)


def part2(): #this function answers part 2
    file = FileHandler("day1/input-day1.txt")
    my_file = file.read_file()
    new_file = my_file.split("\n")
    windows = []
    counter = 0

    for i, x in enumerate(new_file):
        if i == 0 or i == (len(new_file)-1):
            pass
        else:
            pre = new_file[i-1]
            post = new_file[i+1]
            total = int(pre) + int(x) + int(post)
            windows.append(total)

    for i,x in enumerate(windows):
        if i == 0:
            pass
        else:
            pre = windows[i-1]
            if int(x) > int(pre):
                counter += 1
        
    print(counter)


part1()
part2()