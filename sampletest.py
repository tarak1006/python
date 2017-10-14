def get_conswords(word):
    vowel={'a','e','i','o','u'}
    res=[]
    i=0
    while i<len(word):
        v=[]
        if word[i].lower() not in vowel:
            for k in range(i,len(word),1):
                if word[k] not in vowel:
                   v.append(word[k])
                else:
                    i=k-1
                    break

            b=''.join(v)
            if b.upper() not in res:
                if b.lower() not in res:
                   res.append(b)
        i+=1

    res=set(res)
    res=list(res)
    res.sort(key=lambda x:x[0].upper(),reverse=True)
    res.sort(key=len,reverse=True)
    return res[:3]
print get_conswords("Pepper")

# write your own tests
#def test_get_conswords():
    #get_conswords("Pepper")
    #assert ["NGH", "fly", "gh"] == get_conswords( "flyiNGHigh")
    #assert [] == get_conswords("aoi")



