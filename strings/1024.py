# https://www.urionlinejudge.com.br/judge/pt/problems/view/1024
# -*- coding: utf-8 -*-
from math import ceil

n = int(input())
for i in range(n):
    msg = str(input())
    msg2 = ''
    for x in msg:
        if (x.isalpha() == True):
            msg2 += chr(ord(x) + 3)
        else:
            msg2 += x
    msg3 = msg2[::-1]
    s = ceil(len(msg3)/2)
    msg4 = msg3[-s:]
    msg5 = ''
    for y in msg4:
        msg5 += chr(ord(y) - 1)
    emsg = msg3.replace(msg4, msg5)
    print(emsg)
