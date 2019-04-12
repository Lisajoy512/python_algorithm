def longestCommonPrefix(strs) -> str:
    if strs == []:
        return ""
    result = ""
    strs.sort(key=len)
    for i in range(len(strs[0])):
        flag = True
        for j in range(1, len(strs)):
            if strs[j][i] != strs[0][i]:
                flag = False
                break
        if flag:
            result = result + (strs[0][i])
        else :
            break
    return result

if __name__ == "__main__":
    print(longestCommonPrefix(["aca","cba"]))