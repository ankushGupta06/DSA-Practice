def house_robbery_recursive(nums):
    def robbery(i):
        if i >= len(nums):
            return 0
        pick = nums[i] + robbery(i+2)
        not_pick = robbery(i+1)
        return max(pick, not_pick)
    return robbery(0)

def house_robbery(nums):
    dp = [-1]*len(nums)
    def robbery(i):
        if i >= len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]
        pick = nums[i] + robbery(i+2)
        not_pick = robbery(i+1)
        dp[i] = max(pick,not_pick)
        return dp[i]
    return robbery(0)

def house_robbery_bottom_up(nums):
    dp = [-1]*(len(nums)+1)
    dp[0] = nums[0]
    for i in range(1,len(nums)):
        pick = 0
        if i > 1:
            pick = nums[i] + dp[i-2]
        else:
            pick = nums[i]
        not_pick = dp[i-1]
        dp[i] = max(pick,not_pick)
    return dp[len(nums)-1]

def house_robbery_optimized(nums):
    second = 0
    prev = nums[0]
    for i in range(1,len(nums)):
        pick = nums[i] + second
        not_pick = prev
        curr = max(pick,not_pick)
        second = prev
        prev = curr
    return prev
            

print(house_robbery_recursive([2,7,9,3,1]))
print(house_robbery([2,7,9,3,1]))
print(house_robbery_bottom_up([2,7,9,3,1]))
print(house_robbery_optimized([2,7,9,3,1]))