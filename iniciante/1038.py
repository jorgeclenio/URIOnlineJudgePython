# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038
# -*- coding: utf-8 -*-
a, b = map(int, input().split())

if a == 1:
    t = b*4.00
    print(f'Total: R$ {t:.2f}')
elif a == 2:
    t = b*4.50
    print(f'Total: R$ {t:.2f}')
elif a == 3:
    t = b*5.00
    print(f'Total: R$ {t:.2f}')
elif a == 4:
    t = b*2.00
    print(f'Total: R$ {t:.2f}')
elif a == 5:
    t = b*1.50
    print(f'Total: R$ {t:.2f}')
