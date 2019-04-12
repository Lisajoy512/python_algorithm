def isPalindrome(x:int):
    strX = str(x)
    reveseX = strX[::-1]
    if strX == reveseX:
        return True
    else:
        return False

def isPalindrome2(x:str):
    list = x.split("->")
    # strX = x.replace("->","")
    reveseX = list[::-1]
    if list == reveseX:
        return True
    else:
        return False

if __name__ == "__main__":
    print(isPalindrome2("1->2->1"))