# def nextGreaterElement(nums1, nums2):
#     result = []
#     for num1 in nums1:
#         index = nums2.index(num1) + 1
#         while index < len(nums2):
#             if nums2[index] > num1:
#                 result.append(nums2[index])
#                 break
#             index = index + 1
#         if index == len(nums2):
#             result.append(-1)
#     return result

def nextGreaterElement(nums1, nums2):
    if len(nums1) == 0 or len(nums2) == 0:
        return []
    hashmap = {}
    list = []
    for n in nums2:
        if len(list) == 0 or n < list[-1]:
            list.append(n)
        else :
            while len(list) > 0 and n > list[-1]:
                hashmap[list[-1]] = n
                list.pop()
            list.append(n)
    list = []
    for n in nums1:
        if hashmap.get(n) == None:
            list.append(-1)
        else :
            list.append(hashmap[n])
    return list

if __name__ == "__main__":
    print(nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))