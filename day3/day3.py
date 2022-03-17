

from tabnanny import check


data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

my_file = open("day3/input-day.txt", "r")

def part1():
    mylist = my_file.read().split("\n")
    check_list = []
    gamma_rate = ""
    epsilon_rate = ""
    bit = 0
    while bit < len(mylist[0]):
        for i in mylist:
            check_list.append(int(i[bit]))
        if sum(check_list) > (len(mylist)*0.5):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
        bit += 1
        check_list.clear()

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))

def part2():
    mylist = data.split("\n")
    check_list = []
    gamma_rate = []
    epsilon_rate = []
    bit = 0
    while bit < len(mylist[0]):
        for i, x in enumerate(mylist):
            check_list.append(int(x[bit]))
        if sum(check_list) >= (len(mylist)*0.5):
            for i in mylist:
                if i[bit] == "1":
                    gamma_rate.append(i)
                else:
                    epsilon_rate.append
                gamma_rate += "1"
                epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
        bit += 1
        check_list.clear()


def oxygen_generator_rating():
    mylist = data.split("\n")
    check_list = []
    temp_list = []
    o_gen = []
    bit = 0
    while bit < len(mylist[0]):
        if len(mylist) != 1:
            for i in mylist:
                print(f"round {bit}: {i}")
                check_list.append(int(i[bit]))
            if sum(check_list) >= (len(mylist)*0.5):
                for i in mylist:
                    if "0" == i[bit]:
                        mylist.remove(i)
            else:
                for i in mylist:
                    if "1" == i[bit]:
                        mylist.remove(i)
            bit += 1
            check_list.clear()
    print(mylist)


oxygen_generator_rating()