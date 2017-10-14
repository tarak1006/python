#!/bin/python3

import sys
import string

s = input().strip()
n = int(input().strip())
d = dict(zip(list(string.ascii_lowercase), range(1, 27)))
l_zeros = [0] * 26;
res = dict(zip(list(string.ascii_lowercase), l_zeros))
for i in range(len(s)):
    if res[s[i]] == 0:
        res[s[i]] = res[s[i]] + 1;
        while (i + 1 < len(s) and res[s[i]] == res[s[i + 1]]):
            res[s[i]] = res[s[i]] + 1;
            i+=1;
    else:
        c = 1;
        while (i + 1 < len(s) and res[s[i]] == res[s[i + 1]]):
            c = c + 1;
            i+=1;
        if (c > res[s[i]]):
            res[s[i]] = c;
print("haii")
for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    flag = 0
    for key, value in res:
        if (x % d[key] == 0 and x / d[key] <= value):
            flag = 1
            print("Yes")
    if flag == 0:
        print("No")


