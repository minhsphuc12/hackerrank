s = 'aba'
output = [0,3]

def palindromeIndex(s):

    def check_palindrome(s):
        return s == s[::-1]
    if check_palindrome(s):
        return -1
    for i in range(len(s)):
        # print(i, check_palindrome(s[:i]+s[(i+1):]))
        if check_palindrome(s[:i]+s[(i+1):]):
            return i
    return -1

palindromeIndex(s)

# for i in range(len(s)):
#     print(i)
#     check_palindrome(s[:i]+s[(i+1):])

def palindromeIndex(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if is_palindrome(s[left+1:right+1]):
                return left
            if is_palindrome(s[left:right]):
                return right
            return -1  
        left += 1
        right -= 1
    return -1  

palindromeIndex('cacd')
