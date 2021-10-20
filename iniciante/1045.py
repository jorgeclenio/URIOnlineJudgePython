# https://www.urionlinejudge.com.br/judge/pt/problems/view/1045
# -*- coding: utf-8 -*-
a, b, c = list(map(float, input().split()))
t = [a, b, c]

t.sort(reverse=True)

if t[0] >= t[1] + t[2]:
    print('NAO FORMA TRIANGULO')
elif (t[0] * t[0]) == (t[1] * t[1]) + (t[2] * t[2]):
    print('TRIANGULO RETANGULO')
elif (t[0] * t[0]) > (t[1] * t[1]) + (t[2] * t[2]):
    print('TRIANGULO OBTUSANGULO')
elif (t[0] * t[0]) < (t[1] * t[1]) + (t[2] * t[2]):
    print('TRIANGULO ACUTANGULO')
if t[0] == t[1] and t[1] == t[2]:
    print('TRIANGULO EQUILATERO')
elif t[0] == t[1] or t[1] == t[2]:
    print('TRIANGULO ISOSCELES')
