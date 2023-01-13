
with open('1.in', 'r') as f:
    lines = f.read().splitlines()

#    print(lines)

listt = [line.rstrip() for line in open('1.in')]
#print(listt)

cal = []

temp = 0

for i in listt:
    if i is not '':
        temp += int(i)
    
    else:
        cal.append(temp)
        temp = 0

cal.sort(reverse=True)
print(cal[0] + cal[1] + cal[2])


