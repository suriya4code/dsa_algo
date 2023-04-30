#https://leetcode.com/problems/two-sum/

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,7,11,15]
target = 9

def solve(nums, target):
    hm = {}
    for i in range(len(nums)):
        if hm.get(target-nums[i]) != None:
            return [ hm.get(target-nums[i]), i ]
        else:
            hm[nums[i]] = i


print(solve(nums, target))