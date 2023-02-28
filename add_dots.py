def add_dots(s):
    result=""
    for ch in s:
        result+=ch
        result+='.'
    return result

def remove_dots(s):
    result=""
    for ch in s:
        if (ch!='.'):
            result+=ch
    return result
        
s=input("Enter a string please: ")
s=add_dots(s)
print('added dots', s)
s=remove_dots(s)
print('removed dots', s)


