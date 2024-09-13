def is_balanced(s):
    if s.count('(') == s.count(')'):
        return True
    return False

def is_right(s):
    stack = []
    for i in s:
        stack.append(i)
        while len(stack) > 1 and stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()
    if stack:
        return False
    return True

def solution(p):
    if p == '':
        return ''
    for i in range(1, len(p)+1):
        if (is_balanced(p[:i])) and (is_balanced(p[i:])):
            if is_right(p[:i]):
                return p[:i] + solution(p[i:])
            else:
                r = ''
                for k in p[:i][1:-1]:
                    if k == '(':
                        r += ')'
                    else:
                        r += '('
                return '(' + solution(p[i:]) +')' + r