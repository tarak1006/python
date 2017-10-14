__author__ = 'Kalyan'

notes = '''
Python has a good api to deal with text and binary files. We explore that
in this module.

Use help(file.XXX) to find help on file method XXX (tell, seek etc.)
'''

'''
FILE I/O

Modes	Description
r	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
rb	Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
r+	Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
rb+	Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
w	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
wb	Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist,
    creates a new file for writing.
w+	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist,
    creates a new file for reading and writing.
wb+	Opens a file for both writing and reading in binary format.
    Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
a	Opens a file for appending. The file pointer is at the end of the file if the file exists.
    That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
ab	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists.
    That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
a+	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists.
    The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
ab+	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists.
    The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'''

'''
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     open for exclusive creation, failing if the file already exists
'a'     open for writing, appending to the end of the file if it exists
'b'     binary mode
't'     text mode (default)
'+'     open a disk file for updating (reading and writing)
'U'     universal newlines mode (deprecated)
'''


from placeholders import *

import inspect
import os

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir

def get_temp_dir():
    module_dir = get_module_dir()
    temp_dir = os.path.join(module_dir, "tempfiles")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir

# open files generated as a part of the tests. Allow them to be in a different dir via DATA_DIR
def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)

#opens a file from the module directory for reading. These are input files that are part of course material
def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    z= mod_dir
    test_file = os.path.join(mod_dir, file)
    t=test_file
    return open(test_file, mode)


def test_file_readlines():
    f = open_input_file("unit6_input_data.txt")
    lines = f.readlines()# this methid returns a list of strings
    assert ['one\n','two\n','three\n','four\n','five\n']== lines # here \n is compulsory

def test_file_read():
    f = open_input_file("unit6_input_data.txt")
    data = f.read()# this method returns the whole data as one string with no spaces between them
    assert 'one\ntwo\nthree\nfour\nfive\n' == data

def test_file_end():
    f = open_input_file("unit6_input_data.txt")
    s = f.read() # read till end.
    assert '' == f.read()# the object f has already read the whole file , so nothing more to READ
    assert '' == f.read()# f has already reached EOF

def test_file_read_binary():
    f = open_input_file("unit6_input_data.txt", "rb")
    lines = f.readlines()
    assert ['one\r\n','two\r\n','three\r\n','four\r\n','five\r\n'] == lines
    f.seek(0, 0)# how does this work ?
    data = f.read()
    assert 'one\r\ntwo\r\nthree\r\nfour\r\nfive\r\n' == data

def test_file_windows_newlines():
    f = open_temp_file("newlines_tmp.txt", "wb")
    f.write("one\r\ntwo\rthree\n")
    f.close()

    f = open_temp_file("newlines_tmp.txt", "rt")

    assert "one\ntwo\rthree\n" == f.read()
    f.close()

    f = open_temp_file("newlines_tmp.txt", "rb")
    data = f.read()# the whole data in the file is read here and stored as a string
    assert "" == f.read()

    #windows behavior : http://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files

def test_file_universal_newlines():
    f = open_temp_file("newlines_tmp.txt", "wb")
    f.write("one\r\ntwo\rthree\n")
    f.close()

    f = open_temp_file("newlines_tmp.txt", "rU")

    assert 'one\ntwo\nthree\n' == f.read()
    assert ('\r','\n','\r\n') == f.newlines# will return a tuple

def test_file_readline():
    f = open_input_file("unit6_input_data.txt")
    lines = []
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)

    assert ['one\n','two\n','three\n','four\n','five\n'] == lines

#files can be used as iterable objects!
def test_file_iteration():
    f = open_input_file("unit6_input_data.txt")
    lines = []
    for x in f:# x holds the value of each line
        lines.append(x)
    assert ['one\n','two\n','three\n','four\n','five\n'] == lines


def test_file_tell():
    tells = []
    f = open_input_file("unit6_input_data.txt")
    while True:
        line = f.readline()# if f.readline() =='' then EOF has occured
        z=f.tell()
        tells.append(f.tell())

        if not line:# not('') = True
            break
    z=tells
    assert [5,10,17,23,29,29]== tells

def test_file_readlines_tell():
    tells = []
    f = open_input_file("unit6_input_data.txt")
    for line in f.readlines():
        tells.append(f.tell())

    assert [29,29,29,29,29] == tells

def test_file_iteration_tell():
    tells = []
    f = open_input_file("unit6_input_data.txt")
    for line in f:
        tells.append(f.tell())

    assert [29,29,29,29,29] == tells # is there really no difference between readlines and iteration?


def test_file_seek():
    f = open_input_file("unit6_input_data.txt")
    assert 0 == f.tell()
    f.read()
    assert 29 == f.tell()
    assert '' == f.read()

    f.seek(0, 0)
    assert 'one\ntwo\nthree\nfour\nfive\n' == f.read()
    f.seek(5, 2)

    z=f.read()
    assert 'e\n' == f.read()

    f.seek(-2, 1)
    assert '\n' == f.read()

#windows has a few newlines quirks.
def test_file_write_text():
    f = open_temp_file("test_write.txt", "w") # same as "wt"
    f.write("one\ntwo\nthree\n")
    f.close()

    f = open_temp_file("test_write.txt", "rb")
    assert "one\r\ntwo\r\nthree\r\n" == f.read()

    f = open_temp_file("test_write.txt", "rt")

    assert "one\ntwo\nthree\n" == f.read()


def test_file_write_binary():
    f = open_temp_file("test_write.txt", "wb")
    f.write("one\ntwo\nthree\n")
    f.close()

    f = open_temp_file("test_write.txt", "rb")
    assert "one\ntwo\nthree\n" == f.read()#???????????????????????????????????????????????????????????

    f = open_temp_file("test_write.txt", "rt")
    assert "one\ntwo\nthree\n" == f.read()


# It is generally a good practice to close files after their use is over
def test_file_close():
    f = open_input_file("unit6_input_data.txt")
    assert False == f.closed
    try:
        lines = [line.strip() for line in f.readlines()]
    finally:
    # putting it in finally so that it is closed even if an exception is raised
        f.close()
    assert True == f.closed

# http://effbot.org/zone/python-with-statement.htm
# you can close files with a 'with' statement irrespective of exceptions.
# This is similar to using statement in c#
def test_with_statement():
    try:
        with open_input_file("unit6_input_data.txt") as f:
            assert True == f.closed
            raise Exception("some random exception")
    except Exception as ex:
        print ex
        pass

    assert True == f.closed


#https://docs.python.org/2/library/stdtypes.html#file-objects
def test_file_iteration1():
    with open_input_file("unit6_input_data.txt") as f:
        lines = []
        # we are walking through f as an iterator!!
        for line in f:
            lines.append(line.strip())
        assert ['one','two','three','four','five'] == lines

        lines = []
        for line in f:
            lines.append(line.strip())
        # what happened here? read the link i gave above.
        assert [] == lines

# a common pattern to load files into an in memory list
# after doing something on each line (for e.g. strip and upper in this case)
def test_file_iteration2():
    def process(input):
        return input.strip().upper()

    with open_input_file("unit6_input_data.txt") as f:
        data = [process(line) for line in f]
        assert ['ONE','TWO','THREE','FOUR','FIVE'] == data


three_things_i_learnt = """
-
-
-
"""