# Exercício 1 - Função Return Fatorial
 
def fatorial(numero):
     if numero < 0:
         return 'Número inválido! Insira um número positivo.'
     else:
         fatorial = 1
         contador = 1
         
         while contador <= numero:
             fatorial *= contador #1*1=1, 1*2=2, 2*3=6, 6*4=24, 24*5=120
             contador += 1

         return fatorial

fatorial = fatorial(5)
print(f'O fatorial de 5 é {fatorial}')

# Exercício 2 - Função Return Gera um número aleatório entre 1 e 100
import random         

def gera_numero_aleatorio():
    return random.randint(1, 100) 

f = gera_numero_aleatorio()
print(f'O número aleatório gerado foi {f}')
