def mirror(str):
    new_str = []
    for i in range(len(str)):
        new_str.append(str[len(str)-1-i])
    new_str = "".join(new_str)
    return new_str
print (mirror('Mississippi'))
