from math import radians, sin, tan, cos
angulo = float(input('digite um ângulo: '))
seno = sin(radians(angulo))
print('o seno do ângulo {} é {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o cosseno do ângulo {} é {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('a tangente do ângulo {} é {:.2f}'.format(angulo, tangente))
