def threeSum(nums):
    nums.sort()
    results = []
    i=0
    while i < len(nums):
        tmp = nums[i+1:]
        result = newTwoSum(tmp,-nums[i])
        if len(result) > 0:
            results.append((nums[i],tmp[result[0]],tmp[result[1]]))
        while i+1<len(nums) and nums[i] == nums[i+1]:
            i+=1
        i += 1
    return results

def newThreeSum(nums):
    nums.sort()
    res = []
    i = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] > nums[i - 1]:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
    return res

# 不重复
def twoSum(nums, target):
    if len(nums) == 0 :
        return None
    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = i
    for i in range(len(nums)):
        if target-nums[i] in dict.keys() and dict[target-nums[i]] != i :
            return [i,dict[target-nums[i]]]
    return None

# 可重复
def newTwoSum(nums, target):
    if len(nums) == 0 :
        return None
    # nums.sort()
    result = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                result.append((i,j))
    return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    # print(newTwoSum(nums, 0))
    print(threeSum(nums))
    # nums = [0, 1, 4, -2, -1]
    # target = 0
    # print(twoSum(nums,target))
