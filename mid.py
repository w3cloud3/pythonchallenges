def mid(s):
    l=len(s)
    iseven= (l%2 == 0)
    m=int(l/2)
    result=""
    if (not iseven):
        result=s[m]
    return result
    
s=input("Enter a string: ")
result=mid(s)
print("Result: ", result)

