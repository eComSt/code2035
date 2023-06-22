def is_palindrome(s):
    return s == s[::-1]


def is_palindrome2(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l - i - 1]:
            return False
    return True


print( is_palindrome2("helloolleho"))