text = '~iFsozwvpjhw`hik5tnbgbaxfpGbffYe|shfuhermzcisrwy'


def mix(text):
    string = text[::2]
    string = "".join(chr(ord(string[x])-1)
                     for x in range(len(string))
                     if x%2 == 0 else chr(ord(string[x])-2))
    flag = string[::-1]
    return(flag)
    

print(mix(text))
