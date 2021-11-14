def palindrome(x):
    reverseNum = ""
    num = str(x)
    print(num)
    for i in range(len(num)):
        reverseNum = num[i] + reverseNum
    print(reverseNum)
    if reverseNum == num:
        return True
    return False

print(palindrome(121))