# https://www.urionlinejudge.com.br/judge/pt/problems/view/1035
# -*- coding: utf-8 -*-
x = input().split()
a, b, c, d = x

A = int(a)
B = int(b)
C = int(c)
D = int(d)

if (B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
