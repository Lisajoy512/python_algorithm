# 第一种方式，逆序pop
# def removeElement(self, nums: List[int], val: int) -> int:
#     for i in range(len(nums)-1,-1,-1):
#         if nums[i] == val:
#             nums.pop(i)
#     return len(nums)

def removeElement(nums, val: int) -> int:
    cur = 0
    tail = -1
    while cur<len(nums):
        if nums[cur] != val:
            tail = tail + 1
            nums[tail] = nums[cur]
            cur = cur + 1
        else :
            cur = cur + 1
    return tail + 1

if __name__ == "__main__":
    print(removeElement([2,2,2,3],3))