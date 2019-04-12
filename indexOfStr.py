def strStr( haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    flag = False
    index = -1
    i = 0
    j = 0
    while i < len(needle) and j < len(haystack):
        if needle[i] == haystack[j]:
            if flag == False:
                index = j
                flag = True
            i = i + 1
            j = j + 1
        else:
            if flag:
                j = index
                index = -1
                flag = False
            # 这个else就是一个优化点。如果flag之前就为false，说明下次index肯定只会在这次的index之后
            else :
                index = index + 1
            i = 0
            j = j + 1

    if i == len(needle):
        return index
    else:
        return -1

if __name__ == "__main__":
    print(strStr("mississippi","issip"))