def isPalindrome(x):
    if x<0:
        return False
    x_temp = x
    x_reversed = 0
    while x_temp>0:
        x_reversed=x_reversed*10+x_temp%10
        x_temp = x_temp//10
    return x==x_reversed


print(isPalindrome(-121))
