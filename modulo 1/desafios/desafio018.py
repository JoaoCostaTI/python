from math import sin, cos, tan, radians

angulo = float(input('Informe um angulo: '))

angulo_radianos = radians(angulo)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f'O angulo {angulo}°\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')


