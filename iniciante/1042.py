# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042
# -*- coding: utf-8 -*-
a, b, c = list(map(int, input().split()))
lista = [a, b, c]
lista.sort(reverse=True)

print(f'{lista[0]}\n{lista[1]}\n{lista[2]}\n')
print(f'{a}\n{b}\n{c}')
