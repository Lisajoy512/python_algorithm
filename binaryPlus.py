def addBinary(a: str, b: str) -> str:
    l, s = [], []
    if len(a) > len(b):
        l, s = a, b
    else:
        l, s = b, a
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) == 1:
            result = plusOne(l[:i + 1])
            l.replace(l[:i + 1],plusOne(l[:i + 1]))
    return l

def plusOne(s: str) -> str:
    a = list(s)
    if a == []:
        return ""
    i = len(a) - 1
    while i >= 0:
        if a[i] == '0':
            a[i] = '1'
            break
        else:
            a[i] = '0'
            i = i - 1
    if i < 0:
        a.insert(0, '1')
    return "".join(a)


if __name__ == "__main__":
    print(addBinary('11','1'))