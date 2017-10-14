def transform_word(word):
    vowel = {'a', 'e', 'i', 'o', 'u'}
    v=[]
    c=[]
    res=[]
    n=[]
    m=[]
    for i in word:
        if i.lower() not in vowel:
                    c.append(i)
        else:
                    v.append(i)
    n=list(reversed(c))
    res.extend(n)
    m=list(reversed(v))
    res.extend(m)
    b=''.join(res)
    k=[]
    k.append(b[0])
    for i in range(1,len(b)):
        if b[i].lower() !=b[i-1]:
            if b[i].upper() != b[i - 1]:

              k.append(b[i])
    h=''.join(k)

    return h



print transform_word('ApaPle')