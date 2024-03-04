# We define super digit of an integer x using the following rules:

# Given an integer, we need to find the super digit of the integer.

# If x has only 1 digit, then its super digit is x.
# Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
# For example, the super digit of 9875 will be calculated as:

# super_digit(9875)   	9+8+7+5 = 29 
# super_digit(29) 	2 + 9 = 11
# super_digit(11)		1 + 1 = 2
# super_digit(2)		= 2  

def superDigit(n, k):
    len_n = len(n)

    if len_n == 1:
        return int(n)
    else:
        next_n = str(k*sum([int(x) for x in n]))
        print(next_n)
        return superDigit(next_n, 1)

n,k = '9875', 4
n,k = '123', 3
n,k = '9875', 4
superDigit(n,k)

x = (int(n) * k) % 9
print(x if x else 9)
