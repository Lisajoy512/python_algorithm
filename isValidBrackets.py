def isValid(s: str) -> bool:
    l = []
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            l.append(ch)
            print(l)
        elif ch == ')':
            x = l[-1]
            if len(l) == 0 or x != '(':
                return False
            else:
                l.pop()
        elif ch == ']':
            if len(l) == 0 or l[0:2] != '[':
                return False
            else:
                l.pop()
        elif ch == '}':
            if len(l) == 0 or l[0:2] != '{':
                return False
            else:
                l.pop()
        else:
            continue
    if len(l) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(isValid("()"))