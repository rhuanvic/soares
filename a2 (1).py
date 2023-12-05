import os 
os.system('cls')

acesso = {"1234" : "ana", "4321" : "pedro"}
matricula = input('matricula ')

if matricula in acesso.keys():
    print('Hello ', acesso.get(matricula))
else:
   print('erro, faltam 2 tentativas')
   matricula = input('matricula ')
   repetir = 2

   while repetir > 0:        
        repetir -= 1
        if matricula in acesso.keys():
         print('ola ', acesso.get(matricula))
         break      
        elif matricula not in acesso.keys() and repetir>0:
         print('vc tem', repetir, 'tentativas')
         matricula = input('matricula')
        elif matricula not in acesso.keys() and repetir==0:
         print("acabou as")                