def romanToInt(s: str) -> int:
    sum = []
    for ch in s:
        if ch == 'I':
            sum.append('I')
        elif ch == 'V':
            if len(sum) > 0 and sum[-1] == 'I':
                sum.pop()
                sum.append('4')
            else:
                sum.append('V')
        elif ch == 'X':
            if len(sum) > 0 and sum[-1] == 'I':
                sum.pop()
                sum.append('9')
            else:
                sum.append('X')
        elif ch == 'L':
            if len(sum) > 0 and sum[-1] == 'X':
                sum.pop()
                sum.append('40')
            else:
                sum.append('L')
        elif ch == 'C':
            if len(sum) > 0 and sum[-1] == 'X':
                sum.pop()
                sum.append('90')
            else:
                sum.append('C')
        elif ch == 'D':
            if len(sum) > 0 and sum[-1] == 'C':
                sum.pop()
                sum.append('400')
            else:
                sum.append('D')
        elif ch == 'M':
            if len(sum) > 0 and sum[-1] == 'C':
                sum.pop()
                sum.append('900')
            else:
                sum.append('M')

    result = 0
    for ch in sum:
        if ch == 'I':
            result = result + 1
        elif ch == 'V':
            result = result + 5
        elif ch == 'X':
            result = result + 10
        elif ch == 'L':
            result = result + 50
        elif ch == 'C':
            result = result + 100
        elif ch == 'D':
            result = result + 500
        elif ch == 'M':
            result = result + 1000
        else:
            result = result + int(ch)
    return result

if __name__ == "__main__":
    print(romanToInt("III"))