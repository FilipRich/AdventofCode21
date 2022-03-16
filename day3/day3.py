from math import gamma


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


mylist = data.split("\n")
check_list = []
gamma_rate = ""
epsilon_rate = ""
bit = 0
while bit < 5:
    for i, x in enumerate(mylist):
        check_list.append(int(x[bit]))
    if sum(check_list) > (len(mylist)*0.5):
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
    bit += 1
    check_list.clear()



print(gamma_rate)
print(epsilon_rate)


