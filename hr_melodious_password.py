import string
print(list(string.lowercase))
consonant_list=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
vowel_list=['a','e','i','o','u']

def vowels(res_str,len):
    if len==1:
        for i in vowel_list:
            print(res_str+i)
    else:
        for i in vowel_list:
            consonants(res_str+i,len-1)


def consonants(res_str,len):
    if len==1:
        for j in consonant_list:
            print(res_str+j)
    else:
        for j in consonant_list:
            vowels(res_str+j,len-1)


n=int(input())
for i in range(n):
    res=''
    vowels(res,n)
for i in range(n):
    res=''
    consonants(res,n)




