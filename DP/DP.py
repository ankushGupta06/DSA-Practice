# finding nth fibonacci number using dynamic programming

def recursive_fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return recursive_fibonacchi(n-1) + recursive_fibonacchi(n-2)

# top-down approach (memoization)
def fibonacchi_top_down(n):
    if dp[n] != -1:
        return dp[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    dp[n] = fibonacchi_top_down(n-1) + fibonacchi_top_down(n-2)
    return dp[n]

n = 10
dp = [-1]*(n+1)

# bottom-up approach (tabulation)
def fibonacchi_bottom_up(n):
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# tabulation space optimization
def fibonacchi_bottom_up_optimized(n):
    first = 0
    second = 1
    for i in range(2,n+1):
        curr = first + second
        first = second
        second = curr
    return second

print(recursive_fibonacchi(n))
print(fibonacchi_top_down(n))
print(fibonacchi_bottom_up(n))
print(fibonacchi_bottom_up_optimized(n))