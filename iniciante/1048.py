# https://www.urionlinejudge.com.br/judge/pt/problems/view/1045
# -*- coding: utf-8 -*-
s = float(input())

if s >= 0 and s <= 400:
    p = 0.15
    sr = s+(s*p)
elif s >= 400.01 and s <= 800.00:
    p = 0.12
    sr = s+(s*p)
elif s >= 800.01 and s <= 1200.00:
    p = 0.10
    sr = s+(s*p)
elif s >= 1200.01 and s <= 2000.00:
    p = 0.07
    sr = s+(s*p)
elif s > 2000.00:
    p = 0.04
    sr = s+(s*p)

print(f'Novo salario: {sr:.2f}')
print(f'Reajuste ganho: {sr-s:.2f}')
print(f'Em percentual: {p*100:.0f} %')
