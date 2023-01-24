from random import randint
from time import sleep


def jogar():  
  def linha():
    print('\n'+'=+'*20)

    
  def configura_palavra():
    frutas = []
    with open("frutas.txt") as arquivo:
      for linha in arquivo:
        frutas.append(linha[0:-1].upper())  
    numero = randint(0,len(frutas)-1)
    
    word = frutas[numero]  
    return word

  
  def mostra_palavra(word, right_letters):
    sleep(0.4)
    print('\nPalavra:', end=' ', flush=True)
    for c, p in enumerate(word):
      sleep(0.3)
      if (p in right_letters):
        print(f'{p} ', end='', flush=True)
      else:
        print('_ ', end='', flush=True)
    print()

  
  def mostra_tentativas_erradas(wrong_attempts):
    if(len(wrong_attempts) > 0):
      print('\nTentativas erradas:', end=' ', flush=True)
      for l in wrong_attempts:
        sleep(0.3)
        print(f'{l}', end=' ', flush=True)  
  
  
  def realiza_tentativa(right_letters, wrong_attempts):
    while True:
      tentativa = input('Digite uma letra: ').strip().upper()
      if(tentativa == '' or tentativa.isalnum()):
        if(tentativa.isalpha() == False):
          print('Por favor realize a tentativa corretamente.',end=' ')
        elif(tentativa not in right_letters and tentativa not in wrong_attempts):
          break
        else:
            print('Você já fez essa tentativa, faça uma diferente.\n')
      sleep(0.3)
    return tentativa

  
  def tenta_palavra(attempt, word):
    if(attempt != word):
      return True

  
  def tenta_letra(attempt, word):
    conta_letra = word.count(attempt)
    if(conta_letra == 0):
      return True
          
  
  def errou_tentativa(attempt, wrong_attempts):
    wrong_attempts.append(attempt)
    return wrong_attempts
  
  
  def desenha_forca(num):
    sleep(0.6)
  
    print("  _______     ")
    print(" |/      |    ")

    if(num == 6):
      print(" |            ")
      print(" |            ")
      print(" |            ")
      print(" |            ")
      
    if(num == 5):
      print(" |      (_)   ")
      print(" |            ")
      print(" |            ")
      print(" |            ")

    if(num == 4):
      print(" |      (_)   ")
      print(" |       |    ")      
      print(" |       |    ")
      print(" |            ")

    if(num == 3):
      print(" |      (_)   ")
      print(" |      /|    ")
      print(" |       |    ")
      print(" |            ")

    if(num == 2):
      print(" |      (_)   ")
      print(" |      /|\   ")
      print(" |       |    ")
      print(" |            ")

    if(num == 1):
      print(" |      (_)   ")
      print(" |      /|\   ")
      print(" |       |    ")
      print(" |      /     ")

    if (num == 0):
      print(" |      (_)   ")
      print(" |      /|\   ")
      print(" |       |    ")
      print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
  
    if num > 0: print (f'Ainda pode errar {num}x.')
    print()

  
  def finaliza(word,right_letters):
    if acertou:
      linha()
      mostra_palavra(word,right_letters)
      print('\nParabéns, você venceu!')
    else:
      print(f'A palavra era {word}.')
    linha()
  
  
  palavra = configura_palavra()
  qtde_letras_palavra = len(palavra)
  
  letras_certas = list()
  qtde_letras_certas = 0

  tentativas_erradas = list()
  
  vida = 6
  acertou = enforcou = False

#
#    jogo
#
  
  while (not acertou and not enforcou):
    sleep(0.3)
    print('Dica: fruta')
    
    mostra_palavra(palavra, letras_certas)
    mostra_tentativas_erradas(tentativas_erradas)
    print('\n')

    tentativa = realiza_tentativa(letras_certas, tentativas_erradas)
    tamanho = len(tentativa)

    if(tamanho == 1):
      errado = tenta_letra(tentativa, palavra)
    else:
      errado = tenta_palavra(tentativa, palavra)
      if(not errado):
        letras_certas = [x for x in tentativa]
        acertou = True

    if(errado):
      tentativas_erradas = errou_tentativa(tentativa,tentativas_erradas)
      vida -= 1
      enforcou = True if vida == 0 else False
    else:
      letras_certas.append(tentativa)
      qtde_letras_certas += palavra.count(tentativa)
      if(qtde_letras_palavra == qtde_letras_certas):
        acertou = True

    
    if(not acertou):
      desenha_forca(vida)
      
    sleep(0.3)
  
  finaliza(palavra, letras_certas)
  