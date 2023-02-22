def double_letters(s):
    reslut=False
    l=len(s)-1
    if (l>0):
        for i in range(l):
            ch1=s[i]
            ch2=s[i+1]
            if (ch1==ch2):
                reslut=True
                break
    return reslut

s=input("Enter a string: ")
print("double_letters: ", double_letters(s))
