# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012
# -*- coding: utf-8 -*-
entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])
pi = 3.14159

areaTriangulo = (a * c) / 2.0
areaCirculo = pi * pow(c, 2.0)
areaTrapezio = ((a + b) * c) / 2.0
areaQuadrado = pow(b, 2.0)
areaRetangulo = a * b

print("TRIANGULO: {:.3f}".format(areaTriangulo))
print("CIRCULO: {:.3f}".format(areaCirculo))
print("TRAPEZIO: {:.3f}".format(areaTrapezio))
print("QUADRADO: {:.3f}".format(areaQuadrado))
print("RETANGULO: {:.3f}".format(areaRetangulo))
