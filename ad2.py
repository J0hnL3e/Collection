listt = [line.rstrip() for line in open('1.in')]
# A rock, B paper, C scissor
# X rock, Y paper, Z scissor
# 1, 2, 3

# first = ['A', 'B', 'C']
# last = ['X', 'Y', 'Z']
# vals = ['rock', 'paper', 'scissors']

# X lose, Y draw, Z win

outs = ['A X', 'A Y', 'A Z', 'B X', 'B Y', 'B Z', 'C X', 'C Y', 'C Z']
vals = [3, 6, 0, 0, 3, 6, 6, 0, 3]

beat = {'A':'Y', 'B':'Z', 'C':'X'}
tie = {'A':'X', 'B': 'Y', 'C':'Z'}
lose = {'A':'Z', 'B': 'X', 'C':'Y'}

ch = ['X', 'Y', 'Z']
vals2 = [1, 2, 3]
vals4 = [lose, tie, beat]
ends = [0, 3, 6]

dictM = dict(zip(outs, vals))
dictV = dict(zip(ch, vals2))
dict2 = dict(zip(ch, vals4))
outcomes = dict(zip(ch, ends))

sum = 0
for i in listt:
    temp = i.split(' ')
    # already know outcome so only need what to choose
    sum += outcomes[temp[1]]

    choice = dict2[temp[1]][temp[0]]
    sum += dictV[choice]

print(sum)

# sum = 0
# for i in listt:
#     sum += dictM[i]
#     temp = i.split(' ')
#     sum += dictV[temp[1]]
    
# print(sum)


