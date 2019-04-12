def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    str_x = str(x)
    x = ''
    if str_x[0] == '-':
        x += '-'
    x += str_x[::-1].lstrip("0").rstrip("-")
    x = int(x)
    if -2 ** 31 < x < 2 ** 31 - 1:
        return x
    return 0

def reverse2(x):
    if x == 0:
        return x
    num = 0
    pop = 0
    flag = True
    if x < 0:
        flag = False
        x = -x
    while x != 0:
        pop = x%10
        x = int(x/10)
        num = num*10 + pop
    if -2**31<num<2**31:
        if flag :
            return num
        else :
            return -num
    else:
        return 0


if __name__ == "__main__":
    print(reverse2(-123))