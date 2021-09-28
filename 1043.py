# https://www.urionlinejudge.com.br/judge/pt/problems/view/1043
# -*- coding: utf-8 -*-
entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {:.1f}'.format(((a + b) / 2) * c))
