def onlinect(dict):
    ct=0
    for key in dict.keys():
        if (dict[key]=="online"):
            ct=ct+1
        
    return ct
    
statuses = {
    "Alice": "online",
     "Bob": "offline",
     "Eve": "online",
    }

result=onlinect(statuses)
print("Result: ", result)
