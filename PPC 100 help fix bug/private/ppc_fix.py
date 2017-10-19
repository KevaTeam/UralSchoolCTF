from random import choice


flag = 'uralctf{WeEe_fl4g_founD}'
alf = 'qwertyuiopasdfghjklzxcvbnm'
text = '~iFsozwvpjhw`hik5tnbgbaxfpGbffYe|shfuhermzcisrwy'


def inv_mix(flag):
    string = flag[::-1]
    string = "".join(chr(ord(string[x])+1)
                     if x%2 == 0
                     else chr(ord(string[x])+2)
                     for x in range(len(string)))
    string = "".join(x+choice(alf)
                     for x in string)
    return(string)


def mix(text):
    string = text[::2]
    string = "".join(chr(ord(string[x])-1)
                     if x%2 == 0
                     else chr(ord(string[x])-2)
                     for x in range(len(string)))
    string = string[::-1]
    return(string)
    

print(mix(text))

