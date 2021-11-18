
import collections

def has_duplicated(s):
    s = collections.Counter(s)              
    if [i for i in s if s[i] > 1]:          
        return True
    else:
        return False
print(has_duplicated())