def count_syllables(s):
    result=0
    for ch in s:
        if ch=='-':
            result+=1
    return result

s=input('Enter a string hypen to sepeartate sylabels: ')
result=count_syllables(s)
print('Result: ', result)
