# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018
# -*- coding: utf-8 -*-
entrada = int(input())
print(entrada)

n100 = entrada // 100
entrada = entrada - n100*100

n50 = entrada // 50
entrada = entrada - n50*50

n20 = entrada // 20
entrada = entrada - n20*20

n10 = entrada // 10
entrada = entrada - n10*10

n5 = entrada // 5
entrada = entrada - n5*5

n2 = entrada // 2
entrada = entrada - n2*2

n1 = entrada // 1
entrada = entrada - n1*1

print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')
