# https://www.urionlinejudge.com.br/judge/pt/problems/view/1060
# -*- coding: utf-8 -*-
cont = 0
for i in range(1, 7):
    n = float(input())
    if(n > 0):
        cont += 1
print(f'{cont} valores positivos')
