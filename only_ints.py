intType=type(1)
def only_ints(a, b):
    return type(a)==intType and type(b)==intType

print('1, 2', only_ints(1,2))

print('"a", 2', only_ints("a",2))
