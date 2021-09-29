# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020
# -*- coding: utf-8 -*-
entrada = int(input())
a = entrada // 365
entrada = entrada - a*365
m = entrada // 30
entrada = entrada - m*30
d = entrada

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))
