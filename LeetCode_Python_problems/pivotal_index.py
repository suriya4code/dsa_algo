# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

def solve(nums):
    # nums = [1,7,3,6,5,6]

    l = len(nums)

    ps = []
    sum_r = sum(nums)
    # for i in nums:
    #     sum_r += i
    #     ps.append(sum_r)
    # print(ps)

    sum_l = 0
    for i in range(l):
        if i == 0:
            sum_r -= nums[i]
        else:
            sum_l += nums[i-1]
            sum_r -= nums[i]
        if sum_l == sum_r:
            return nums[i]
    return -1
        

print(solve([1,7,3,6,5,6]))