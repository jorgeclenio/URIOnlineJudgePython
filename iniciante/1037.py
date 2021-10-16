# https://www.urionlinejudge.com.br/judge/pt/problems/view/1037
# -*- coding: utf-8 -*-
entrada = float(input())

if entrada >= 0 and entrada <= 25.0000:
    print("Intervalo [0,25]")
elif entrada > 25.0000 and entrada <= 50.0000:
    print("Intervalo (25,50]")
elif entrada > 50.0000 and entrada <= 75.0000:
    print("Intervalo (50,75]")
elif entrada > 75.0000 and entrada <= 100.0000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
