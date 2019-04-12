def maxProduct(nums: [int]) -> int:
    # for i in range(1, len(nums)):
    #     if nums[i] < 0:
    #         nums[i] = nums[i] * min(nums[i - 1], 1)
    #     else:
    #         nums[i] = nums[i] * max(nums[i - 1], 1)
    # return max(nums)
    B = nums[::-1]
    for i in range(1, len(nums)):
        print(nums[i - 1] or 1)
        nums[i] *= nums[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(max(nums), max(B))


if __name__ == "__main__":
    print(maxProduct([2,3,-2,4]))
