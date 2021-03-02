from random import randint
def get_number(seed,number,left,right):
    number = number * 1234 + 1234
    ans = int(str(seed*seed*number)[(number//10) % 10:(number // 10) % 10 + len(str(seed))])
    ans = (((ans - 100000000) * (right - left)) / (9999999999 - 100000000)) + left
    return ans
def get_seed():
    return randint(1000000000,9999999999)