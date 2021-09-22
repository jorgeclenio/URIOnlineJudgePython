# https://www.urionlinejudge.com.br/judge/pt/problems/view/10010
# -*- coding: utf-8 -*-
entrada1 = input().split()
cp1 = int(entrada1[0])
np1 = int(entrada1[1])
vp1 = float(entrada1[2])

entrada2 = input().split()
cp2 = int(entrada2[0])
np2 = int(entrada2[1])
vp2 = float(entrada2[2])

valorTotal = (np1*vp1) + (np2*vp2)

print('VALOR A PAGAR: R$ {:.2f}'.format(valorTotal))
