__author__ = 'Kalyan'

notes='''
 This is a basic problem involving some file reading and writing. You can put what you have learnt in earlier units
 to use here - functions or nested functions, lists, sorting, generators(optional), comprehensions (optional) etc.

1. Review the relevant lessons if you are blocked.
2. Do not modify the given input files :), modify your code to handle them.
3. Write helper routines where as needed.
3. You can write your own test routines like test_sort_words2(), but comment them out before submitting.
'''

import unit6utils

def sort_words(source, destination):
    l=[]
    a=[]
    """
    Sort the words in the file specified by source and put them in the
    file specified by destination. The output file should have only lower
    case words, so any upper case words from source must be lowered.

    Ignore empty lines or lines starting with #
    """
    f=open(source,"rt")
    f2=open(destination,'wt')
    for i in f:
        if '#' not in i and not i.startswith('\n'):
            a.append(i.lower())
    a[-1]=a[-1]+'\n'
    a.sort()
    for i in a:
        f2.write(i)
    f2.close()

def test_sort_words():
    source = unit6utils.get_input_file("unit6_testinput_02.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_02.txt")
    destination = unit6utils.get_temp_file("unit6_output_02.txt")
    sort_words(source, destination)
    result = [word.strip() for word in open(source)]
    print result
    expected = [word.strip() for word in open(expected)]
    print expected

