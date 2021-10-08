# https://www.urionlinejudge.com.br/judge/pt/problems/view/1019
# -*- coding: utf-8 -*-
n = int(input())

hora = n // 60**2
n = n - hora * 60**2

minuto = n // 60
n = n - minuto*60

segundo = n

print(f'{hora}:{minuto}:{segundo}')
