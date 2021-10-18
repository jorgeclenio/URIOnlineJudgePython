# https://www.urionlinejudge.com.br/judge/pt/problems/view/1036
# -*- coding: utf-8 -*-
a, b, c = map(float, input().split())

if a == 0.0 or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    x1 = (- b + (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
    x2 = (- b - (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
