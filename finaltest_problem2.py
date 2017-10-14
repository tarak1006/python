max_marks = 25

problem_notes = '''
Given a sentence transform all words in it according to the following guidelines:

- Move all consonents before the vowels
- The consonents and vowels should be in the reverse order of the original.
- If two equal letters come next to each other in the result (case insensitive duplicates),
  drop the second letter in the source.

For e.g. eagle becomes lgeae ApaPle becomes lpeA (dropped the duplicates)

Additional constraints:
- Preserve the case of the original letters.
- Words are separated by spaces. Drop all non-letters like digits and punctuation
   and special chars in the sentence.
- raise TypeError on non str inputs.
- Note that both the routines below will be tested and scored, so do not rename the methods or change the
decomposition, you can write additional helper routines but the methods given should be coded correctly.

'''

# transforms a single word, no type checking required
def transform_word(word):
    if type(word).__name__!='str':
        raise TypeError
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
    k = []
    k.append(b[0])
    for i in range(1, len(b)):
        if b[i].lower() != b[i - 1]:
            if b[i].upper() != b[i - 1]:
                k.append(b[i])
    h = ''.join(k)

    return h






# uses the above method to get the work done. all type checking etc. goes here
def transform(sentence):
    sentence=sentence.replace(',','')
    s=sentence.split(" ")
    t=[]
    l=''
    for word in s:

        vowel = {'a', 'e', 'i', 'o', 'u'}
        v = []
        c = []
        res = []
        n = []
        m = []
        for i in word:
            b=''
            if i.lower() not in vowel:
                c.append(i)
            else:
                v.append(i)
        n = list(reversed(c))
        res.extend(n)
        m = list(reversed(v))
        res.extend(m)
        b = ''.join(res)
        k = []
        k.append(b[0])
        for i in range(1, len(b)):
            if b[i].lower() != b[i - 1]:
                if b[i].upper() != b[i - 1]:
                    k.append(b[i])
        w = ''.join(k)

        t.append(w)

    for i in range(len(t)):
        o = ''
        for j in t[i]:

            if j.isalpha():
                o+=j
        t[i]=o
    h=' '.join(t)
    return h

print transform("Apple, eagle and SE00e")
def test_transform_word():
    pass
#def test_transform():
    #assert "lpeA lgeae dna SE" == transform("Apple, eagle and SE00e")

