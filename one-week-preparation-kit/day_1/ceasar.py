
s = 'middle-Outz'
k = 2
output = 'okffng-Qwvb'

def caesarCipher(s, k):
    strings = 'abcdefghijklmnopqrstuvwxyz'
    strings_upper = strings.upper()
    c_count = len(strings)
    out = ''
    for c in s:
        # c = 'z'
        if c in strings:
            out += strings[(strings.find(c)+k)%c_count]
        elif c in strings_upper:
            out += strings_upper[(strings_upper.find(c)+k)%c_count]
        else:
            out += c
    return out
