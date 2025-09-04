nota1 = float(input('digite sua 1ª nota  '))
nota2 = float(input('digite sua 2ª nota  '))
nota3 = float(input('digite sua 3ª nota  '))
nota4 = float(input('digite sua 4ª nota  '))

media = (nota1 + nota2 + nota3 + nota4)//4

      
if media >= 7.0:
    print(f'média: {media} - situação :aprovado')
elif media >= 5.0 < 7.0:
    print(f'média: {media} - situação :recuperação')
else:
    print(f'média: {media} - situação :reprovado')

