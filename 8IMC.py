import os
print("Qual o seu imc")
print("Qual a sua Altura?: ")
altura = float(input())

print("Qual o seu Peso?: ")
peso = float(input())

imc = round(peso/altura**2)

os.system('CLS')

if imc <= 18.5:
    
    print ("Magreza")
    print("Va comer")
    print("Resultado:" , imc)

elif 18.5 < imc <= 24.9:
    
    print('Normal')
    print('Continue assim')
    print("Resultado:" , imc)
elif  24.9 < imc <= 30:
    
    print("Sobrepeso")
    print("Se acalme")
    print("Resultado:" , imc)
elif 30 < imc <= 40:
    
    print("Obesidade Morbida")
    print("Resultado:" , imc)
else :
    imc > 40 
    print("Obesidade Grave")
    print("Thais carla?")
    print("Resultado:" , imc)