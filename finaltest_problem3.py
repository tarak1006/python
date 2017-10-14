__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
A number is said to be a magic number in a given base if it is divisible by sum of its digits in that given base.

A few examples:

11 -> is not a magic number in base 10 (since 11 is not divisible by 2)
11 -> is a magic number in base 16 (since 11 in hex is B and sum of digits is 11 (B) and since 11 is divisible by 11)
11 -> is not a magic number in base 2 -> (11 in binary is 1011, sum of digits is 3 and 11 is not divisible by 3)
33 -> is a magic number in base 12 ( it is 29 in base 12, sum of digits is 11 and 33 is divisible by 11)
33 -> is not a magic number in base 10 ( since 33 is not divisible by 6)
255 -> is not a magic number in base 16 (255 is FF in hex, sum of digits is 30, 255 is not divisible by 30)
66 -> is a magic number in base 64 (66 is 12 in base 64, sum of digits is 3, and 66 is divisible by 3)

Write the following routines to determine if a given number is a magic number in a given base and to write
an infinite generator of successive magic numbers in a given base.

Constraints:
- no type checking required.
- raise value error if number <=0 or base < 2
- there is no upper bound on the base, so code appropriately instead of assuming that is less than some hardcoded
upper bound value like 16 or 36.
'''
import string


# returns True if the specified number is a magic number in the given base.
def is_magic(number, base):
    l=number
    str = list(string.digits + string.ascii_uppercase)
    d1 = {i: str[i] for i in range(36)}
    alpha = list(string.uppercase)
    d2 = {j: i + 10 for i, j in enumerate(alpha)}
    str1 = ''
    if number > 0:
        while number > 1:
            num = number % base
            str1 = d1[num] + str1
            number = number / base
            if number == 0 | 1:
                num = number % base
                str1 = d1[num] + str1

    try:
        k = int(str1)
    except ValueError as ve:
        c = 0

        for i in str1:
            if i.isalpha():
               c = c + d2[i]
            else:
                c=c+int(i)
        if l % c == 0:
            return True
        else:
            return False

    e = 0
    while k >0:
        i=k%10
        e += i
        k=k/10
    if l % e == 0:
        return True
    else:
        return False

#print is_magic(11, 10)
#print is_magic(11, 16)
#print is_magic(11, 2)
#print is_magic(33, 12)
# generator that yields the magic numbers in a given base starting from 1 in increasing order.
# use the above method to get this done.
def magic_numbers(base):
    i = base
    while True:
        if is_magic(i, base):
            yield i
        i += 1


# write your own tests.
#def test_is_magic():
   # assert True == is_magic(11, 10)


def test_magic_numbers():
    g=magic_numbers(16)
    c=0
    res=[]
    for i in g:
        c+=1
        res.append(i)
        if c==5:
            break
    print res

