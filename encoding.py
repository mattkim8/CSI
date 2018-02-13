#Problem Set 3, Part II
#Kim, Matthew

def switcher(x):
    string = ''
    for n in x:
        if n == 'a':
            n = 'b'
        elif n == 'b':
            n = 'a'
        elif n == 'e':
            n = '&'
        string += n
    return string

def msg_encoder(x):
    x = switcher(x)
    h = len(x)
    if h%2 == 0:
        a = x[0:h/2]
        b = x[h/2:h+1]
        return b+a
    elif h%2 == 1:
        a = x[0:h/2]
        b = x[(h/2):h/2+1]
        c = x[(h/2+1):h+1]
        return c+b+a
    
def msg_decoder(s):
    string = ''
    for n in s:
        if n == 'b':
            n = 'a'
        elif n == 'a':
            n = 'b'
        elif n == '&':
            n = 'e'
        string += n
        s = string
    h = len(s)
    if h%2 == 0:
        a = s[0:h/2]
        b = s[h/2:h+1]
        return b+a
    elif h%2 == 1:
        a = s[0:h/2]
        b = s[(h/2):h/2+1]
        c = s[(h/2+1):h+1]
        return c+b+a
