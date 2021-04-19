import random

N = int(input(' Input N (10-150)'))
if N > 150:
    N = 150
elif N < 10:
    N = 10

x = random.randint(0, 2**N)
prev = bin(x)[2:].rjust(N,'0')

rule10 = int(input('Input rule (0-255)'))
if rule10 > 255 or rule10 < 0:
    rule10 = 110

rule={}
for i in range(8):
    rule[bin(i)[2:].rjust(3,'0')] = str(rule10 % 2)
    rule10 = rule10 // 2


keys = list(rule.keys())
keys.reverse()
print('-'*N)


for j in range(N):
    print(prev.replace('0',' ').replace('1', 'X'), )
    nxt=[]
    for i in range(N):
        k = prev[i-1]+prev[i]+prev[0 if i==N-1 else i+1]
        nxt.append(rule[k])
    prev = ''.join(nxt)



