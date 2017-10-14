__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''
import string
def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    str=list(string.digits+string.ascii_uppercase)
    d1={i:str[i] for i in range(36)}
    str1=''
    if type(number)!=int:
        raise TypeError
    if type(base)!=int:
        raise TypeError


    if number<0:
        number=number*-1
        while number*-1:
            num=number%base
            str1=d1[num]+str1
            number=number/base
            if number==1:
                num=number%base
                str1=d1[num]+str1
                str1='-'+str1
            elif number == 0:
                str1 = '-' + str1

    if number>0:
        while number>1:
            num=number % base
            str1=d1[num]+str1
            number=number/base
            if number == 0|1:
                num=number%base
                str1=d1[num]+str1
    return str1

def test_convert():
    assert "100" == convert(4,2)
    assert "12" == convert(66,64)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print te