def is_anagram(word1, word2):
    w1 = sorted(word1)
    w2 = sorted(word2)
    w1 = [x.strip(' ') for x in w1]
    w2 = [x.strip(' ') for x in w2]
    if w1 == w2:
        return 'anagram'
    else:
        return 'not anagram'
    
print(is_anagram('пила  ', 'липа'))