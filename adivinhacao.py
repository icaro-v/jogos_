from random import randint
from time import sleep


def jogar():
  def mensagem_inicio():
    sleep(0.6)
    print('Pensei em um número entre 1 e 100...',flush=True)
    print('Será que você consegue adivinhá-lo?\n')
  
    print('''Em qual nível você quer jogar?\n 
    1 --- Fácil
    2 --- Médio
    3 --- Difícil\n''')
    

  def escolha_do_nivel():
    niveis = ['fácil','médio','difícil']
    
    while True:
      nivel = input('Sua escolha [1 / 2 / 3]: ').strip()
      if(nivel == '1' or nivel == '2' or nivel == '3'):
        nivel = int(nivel)
        break
      print('Escolha um número válido.',end=' ')
        
    if (nivel == 1):
      attempts = 10
    elif (nivel == 2):
      attempts = 7
    else:
      attempts = 5

    print(f'\nVocê escolheu o nível {niveis[nivel-1]}, portanto, terá {attempts} tentativas.\nBoa sorte!\n') 
    
    return attempts
    
  
  def print_pontos():
    pontos = "..."
    for p in pontos:
      sleep(0.3)
      print(f'{p}', end='', flush = True)
    sleep(0.3)
    print('\n')
    

  def processa_tentativa(vez,attempted):    
    while True:
      tentativa = input(f'{vez}ª tentativa: ').strip()
      if(tentativa.isnumeric()):
        tentativa = int(tentativa)
        
        if(tentativa not in attempted):
          break
          
        print(f'\nVocê ja tentou o {tentativa}, pense em outro número.')
      else:
        print('Escolha um número válido.', end = ' ')
        
    return tentativa

    
  def resultado(tentado,number,vez,attempts):    
    if (tentado == number):
      print(f'Parabéns, você acertou!.O número era {number}.')
      return True
    elif (vez != attempts):
      if (tentado > number):
        print('Você deve chutar um número menor.')
      else:
        print('Você deve chutar um número maior.')
      print()
    else:
      print(f'O número era {number}.\nFim de jogo.')
      return True
  
  
  num = randint(1,100)
  numeros_ja_tentados = list()

  mensagem_inicio()

  tentativas = escolha_do_nivel()
  
  for n in range(1, tentativas+1):
    num_tentado = processa_tentativa(n,numeros_ja_tentados)
    numeros_ja_tentados.append(num_tentado)
    
    print_pontos()
    
    if(resultado(num_tentado,num,n,tentativas)):
      break
