def capital_indexes(s):
    result=[]
    for i in range(len(s)):
        ch=s[i]
        if (ch.isupper()):
            result.append(i);
    return result
        
    
s=input("Enter a string: ")
res=capital_indexes(s)
print(res)

