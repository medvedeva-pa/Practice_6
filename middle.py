def middle(t):
    t.pop(0)
    t.pop(-1)
    return t
print(middle([7,2,7,8,9,1,0]))