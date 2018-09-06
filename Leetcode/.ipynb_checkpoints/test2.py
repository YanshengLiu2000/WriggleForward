def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    max=''
    dp=[[bool for i in range(len(s))]for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i]=True
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                if i+1==j:
                    dp[i][j]=True
                else:
                    dp[i][j]= dp[i+1][j-1]
            else:
                dp[i][j] = False
        if dp[i][j] is True and j-i>len(max):
            max=s[i:j]
            print(max)
    return dp

s='abba'
dp=longestPalindrome(s)
for i in dp:
    print(i)