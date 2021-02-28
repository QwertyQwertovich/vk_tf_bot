seed = 6561777104
import random
'''def get_number(seed,number):
    a = str(seed)
    b = []
    c = ''
    for i in range(len(a)):
        b.append(a[(i * number) % len(a):] + a[:i * (number) % len(a)])
    #print(b)
    n = a+str(number)
    for i in range(len(a)):
        c = c + a[int(b[i][(int(n[-i]))])]
    return int(c)'''
'''def get_number(seed,number):
    x = bin(seed)[2:]
    for i in range(number):
        a = x[2:] + x[:2]
        b = x[3:] + x[:3]
        c = x[-5:] + x[:-5]
        d = x[-7:] + x[:-7]
        res = int(x,2)+int(a,2)+int(b,2)+int(c,2)+int(d,2)
        x = bin(res)[3:len(str(bin(seed)[2:]))+3]
    return int(x,2)'''
def get_number(seed,number):
    number = number * 1234 + 1234
    return int(str(seed*seed*number)[(number//10) % 10:(number // 10) % 10 + len(str(seed))])
for i in range(0,100000):
    seed = random.randint(1000000000,9999999999)
    print(get_number(seed,i))