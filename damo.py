import os
os.system('cls')

#colocar nome verificar
print('--------Sistema de Contra Cheque----------')
Nome = input('Digite apenas o Primeiro nome: ').strip()
while True:   
    if Nome.isalpha() == False:
        print('-------------')
        print(f'{Nome} errado, somente Letras ou/e Somente o primeiro nome ')
        Nome = input('Digite novamente o primeiro nome: ')
    elif Nome.isalpha() == True:
        break
os.system('cls')

Sobrenome = input('Digite o Ultimo Sobrenome: ').strip()
while True:   
    if Sobrenome.isalpha() == False:
        print('-------------')
        print(f'{Sobrenome}  errado, somente Letras ou/e Somente sobrenome')
        Sobrenome = input('Digite novamente o ultimo sobrenome: ')
    elif Sobrenome.isalpha() == True:
        break
os.system('cls')

#colocar salario e testar
Salario= input('Digite o salario: ')  
while True:
    try:   
        if Salario.isalpha() == True or float(Salario) < 0 :
            print('----------------')
            Salario = (input('Digite novamente o salario, Somente numeros: '))
        else:
            break
    except ValueError:
        print('----------------')
        Salario = input('Digite novamente o salario, Somente numeros:  ')
os.system('cls')          

#por horas extras e verificar
Hora_extra= input('digite as horas extras do mes no sistema centésimal (ex: 4h30min, vira 4.5): ')
while True:
    try:  

        if Hora_extra.isalpha() == True or float(Hora_extra) < 0:
            print('----------------')
            Hora_extra = input('Digite as horas extras do mês novamente: ')
        else:
            break    
    except ValueError:
        print('----------------')
        Hora_extra = input('Valor invalido, Digite as horas extras do mes : ')  
os.system('cls')             

#por setor e verificar
Setor=input('Digite seu setor(Adm/Operacional) ')
while True:
    listasetor = ("Operacional", "Adm")
    if Setor not in listasetor:
        os.system('cls')
        Setor = input("Escolha inválida, somente as opções(Adm/Operacional)")
    else:
        break
os.system('cls')


if float(Hora_extra) > 4 and Setor == 'Adm':
    Salario_atualizado = 4*4.5 + float(Salario)
    Banco_de_horas= float(Hora_extra) - 4
elif float(Hora_extra)  > 4 and Setor == 'Operacional':
    Salario_atualizado = 4*3.5 + float(Salario)
    Banco_de_horas = float(Hora_extra) - 4
elif float(Hora_extra)  <= 4 and Setor == 'Adm':
    Salario_atualizado = float(Hora_extra)*4.5 + float(Salario)
    Banco_de_horas = 0
elif float(Hora_extra)  <= 4 and Setor == 'Operacional':
    Salario_atualizado = float(Hora_extra)*3.5 + float(Salario)
    Banco_de_horas = 0
else:
    print('erro')
    

print('--------Sistema de Contra Cheque----------')
print('---------FUNCIONARIO---------')
print(f'Nome Completo: {Nome} {Sobrenome}')
print('Salario: R$', Salario_atualizado,'reais')
print('Setor:', Setor)
print('Quantas horas extras:', Hora_extra,'Horas')
print('Banco de horas:', Banco_de_horas,'Horas')
print('------------------')       






'''Media= (float(Nota1) + float(Nota2))/2
if Media >= 7:
    print('Nome:', Nome)
    print('Sua media é:', Media)
    print('Status: Aprovado')
    if Media<= 10 and Media >= 9 :
        print('Conceito: A')
        exit()
    elif Media  < 9 and Media >= 7: 
        print('Conceito: B')
        exit()
elif Media < 7 and Media >= 6:
    print('Nome:', Nome)
    print('Sua media é:', Media)
    print('Status: Recuperação')
    print('Conceito: C')
    exit()
elif Media < 6 and Media >= 0:
    print('Nome:', Nome)
    print('Sua media é:', Media)
    print('Status: Reprovado')
    print('Conceito: D')
    exit()
else:
    print(' Dados errados')'''
                    
                    
                         



