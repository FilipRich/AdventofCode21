

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
    mylist = my_file.read().split("\n")
    oxygen_generator_rating(mylist)
    co2_scrubber_rating(mylist)

    #oxygen_gen = oxygen_gen_list.pop()
    #co2_scubber = co2_scruber_list.pop()

    #print(oxygen_gen + " " + co2_scubber)


def oxygen_generator_rating(file):
    mylist = file
    check_list = []
    temp_list = []
    o_gen = []
    bit = 0
    while bit < len(mylist[0]):
        if len(mylist) != 1:
            for i in mylist:
                check_list.append(int(i[bit]))
            if sum(check_list) >= (len(mylist)*0.5):
                for i in mylist[:]:
                    if i[bit] == "0":
                        print(f"oxygen removing {i}")
                        mylist.remove(i)        
            else:
                for i in mylist[:]:
                    if i[bit] == "1":
                        mylist.remove(i)
            bit += 1
            check_list.clear()
    print(mylist)

def co2_scrubber_rating(file):
    print("Hello")
    mylist = file
    check_list = []
    temp_list = []
    o_gen = []
    bit = 0
    while (bit < len(mylist[0])) and (len(mylist) != 1):
        for i in mylist:
            check_list.append(int(i[bit]))
            print(f"round {bit} val: {i}")
        if sum(check_list) >= (len(mylist)*0.5):
            for i in mylist[:]:
                if i[bit] == "1":
                    print(f"scrubber Removing {i}")
                    mylist.remove(i)
        else:
            for i in mylist[:]:
                if i[bit] == "0":
                    mylist.remove(i)
        bit += 1
        check_list.clear()
    print(mylist)

part2()