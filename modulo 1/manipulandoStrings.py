'''frase = "Curso em Video Python"

print(frase[9::3])
print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))'''

usuario = input('Digite sua senha: ') #senha

while usuario.find('senha') == -1:
    print('Senha incorreta, tente novamente')
    usuario = input('Digite sua senha: ')
print('Senha correta! Pode passar!')