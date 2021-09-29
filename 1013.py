# https://www.urionlinejudge.com.br/judge/pt/problems/view/1013
# -*- coding: utf-8 -*-
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maiorAB = (a + b + abs(a - b)) / 2

if(maiorAB > c):
    print("{:.0f} eh o maior".format(maiorAB))
else:
    print("{:.0f} eh o maior".format(c))
