s = '{[(])}' 
s = '{{[[(())]]}}'
s = '{(([])[])[]}'
s = '{[][]}'
s = '{{([])}}'
s = '{{)[](}}'
s = '{(([])[])[]]}'
s = '[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]'
s = '{{}('
# def isBalanced(s):
#     def pair(a,b):
#         return a+b in ['{}', '[]', '()']
#     if s == '':
#         return 'YES'
#     elif pair(s[0], s[-1]):
#         return isBalanced(s[1:-1])
#     else:
#         return 'NO'

def isBalanced(s):
    def pair(a,b):
        return a+b in ['{}', '[]', '()']
    stack = []
    for c in s:
        # print('c', c)
        if c in ['[', '(', '{']:
            stack.append(c)
            # print(stack)
            continue
        if len(stack) > 0:
            if pair(stack[-1], c):
                stack.pop()
                continue
            else:
                return 'NO'
        return 'NO'
    if len(stack) > 0:
        return 'NO'
    return 'YES'

isBalanced(s)

cases = open('one-week-preparation-kit/day_5/test_cases', 'r').read().split('\n')
results = open('one-week-preparation-kit/day_5/test_cases_result', 'r').read().split('\n')
len(cases) == len(results)
for i in range(len(cases)):
    if isBalanced(cases[i]) != results[i]:
        print(cases[i])
        print(results[i])

cases = ['}][}}(}][))]',
'[](){()}',
'()',
'({}([][]))[]()',
'{)[](}]}]}))}(())(',
'([[)']

for s in cases:
    print(s)
    isBalanced(s)

def isBalanced(s):
    def pair(a,b):
        return a+b in ['{}', '[]', '()']

    l = []
    for c in s:
        if c in ['{', '[', '(']:
            l.append(c)
        elif pair(l[-1], c):
            l.pop()
        else:
            return 'NO'
    return 'YES'
        
s = '{[[]}]'
s = '{[[]]}'
isBalanced(s)

def isBalance(s):
    # Define a mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    open_set = set(['(', '{', '['])  # Set of opening brackets

    stack = []  # Initialize an empty stack

    for char in s:
        if char in open_set:  # If it's an opening bracket, push onto the stack
            stack.append(char)
        elif char in bracket_map:  # If it's a closing bracket
            if not stack:  # If stack is empty, no opening bracket available for match
                return False
            elif stack[-1] == bracket_map[char]:  # If top of stack matches closing bracket
                stack.pop()  # Pop the matching opening bracket from the stack
            else:  # If top of stack does not match closing bracket
                return False
        else:
            # If the character is not a bracket, you can decide whether to ignore it or handle as an error
            pass

    return not stack  # If stack is empty, brackets are correctly matched
