# https://www.urionlinejudge.com.br/judge/pt/problems/view/1133
# -*- coding: utf-8 -*-
n = int(input())
x = 0

for i in range(1, n+1):
    print('{} {} {} PUM'.format(x+1, x+2, x+3))
    x += 4
