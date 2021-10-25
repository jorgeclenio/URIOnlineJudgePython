# https://www.urionlinejudge.com.br/judge/pt/problems/view/1060
# -*- coding: utf-8 -*-
cont = 0
media = 0
for i in range(1, 7):
    n = float(input())
    media += n
    if(n > 0):
        cont += 1
print(f'{cont} valores positivos')
print(f'{media/6:.1f}')
