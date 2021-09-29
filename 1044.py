# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044
# -*- coding: utf-8 -*-
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])

if(a > b):
    if(a % b == 0):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

if (b > a):
    if(b % a == 0):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

if (a == b):
    print("Sao Multiplos")
