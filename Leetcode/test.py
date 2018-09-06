def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if s == '0':
        return 0
    elif len(s) == 1:
        return 1
    dp = [int for i in s]
    dp[-1] = 1 if int(s[-1]) > 0 else 0
    # dp[-2]=2 if int(s[-2:])>10 and int(s[-2:])<=26 else 1
    if int(s[-2:]) == 0:
        dp[-2] = 0
    elif int(s[-2:]) > 10 and int(s[-2:]) <= 26:
        dp[-2] = 2
    else:
        dp[-2] = 1

    for i in range(len(s) - 3, -1, -1):
        if int(s[i:i + 2]) > 10 and int(s[i:i + 2]) <= 26:
            dp[i] = dp[i - 1] + dp[i - 2]
        elif int(s[i:i + 2]) == 0:
            return 0
        elif int(s[i:i + 2]) < 10:
            dp[i] = 0
        elif int(s[i:i + 2]) > 26 and int(s[i:i + 2]) % 10 != 0:
            return 0
        else:
            dp[i] = dp[i - 1] + 1
    return dp[0]

numDecodings('12120')