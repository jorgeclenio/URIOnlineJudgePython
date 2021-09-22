# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009
# -*- coding: utf-8 -*-
nome = input()
salarioFixo = float(input())
totalVendas = float(input())

total = salarioFixo + (totalVendas * 0.15)

print('TOTAL = R$ {:.2f}'.format(total))
