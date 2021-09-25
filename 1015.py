# https://www.urionlinejudge.com.br/judge/pt/problems/view/1015
# -*- coding: utf-8 -*-
import math

entrada1 = input().split()
x1 = float(entrada1[0])
y1 = float(entrada1[1])

entrada2 = input().split()
x2 = float(entrada2[0])
y2 = float(entrada2[1])

distancia = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))

print("{:.4f}".format(distancia))
