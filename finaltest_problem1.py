__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
A 'consword' is a word which has only consonents. For this problem, you have to write code to
return all maximal conswords that are substrings of a given string. A consword is called maximal if it
cannot be extended on either side with a consonent.

Sort the result in descending order of length. In case of a length tie, sort them in descending order
lexicographically (case insensitive)

Examples:
- "Pepper" -> ["pp", "r", "P"]
- "flyiNGHigh" -> ["NGH", "fly", "gh"]
- "aoi"  -> []

Additional Notes/Constraints:
- Only letters (a-zA-Z) are allowed, any other characters like digits or spaces should raise a ValueError
- Non strings should raise a TypeError
- Use python builtins as appropriate.
- Maintain the original casing of the letters.
'''
def get_conswords(word):
    for q in word:
        if type(q).__name__ != 'str':
           raise  ValueError
    if type(word).__name__!='str':
        raise TypeError
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

# write your own tests
def test_get_conswords():
    pass


