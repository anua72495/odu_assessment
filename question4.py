def longest_repeating_subsequence(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]
print(longest_repeating_subsequence("abc")) 
print(longest_repeating_subsequence("aab"))  
print(longest_repeating_subsequence("aabb")) 
print(longest_repeating_subsequence("axxxy")) 

