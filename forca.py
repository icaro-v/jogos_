from random import randint
from time import sleep


def jogar():
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
    print('Palavra:', end=' ', flush=True)
    for c, p in enumerate(word):
      sleep(0.3)
      if (p in right_letters):
        print(f'{p} ', end='', flush=True)
      else:
        print('_ ', end='', flush=True)
    print()

  
  def mostra_letras_erradas(wrong_letters):
    print('\nLetras erradas:', end=' ', flush=True)
    for l in wrong_letters:
      sleep(0.3)
      print(f'{l}', end=' ', flush=True)
    print('\n')
  
  
  
  def realiza_tentativa(right_letters, wrong_letters, word):
    while True:
      letter = input('Digite uma letra: ').strip().upper()
      if(letter == ''):
        print('Não desperdice essa chance tão valiosa com um espaço em branco.')
      else:
        if(letter not in right_letters and letter not in wrong_letters):
          break      
        print('Você ja tentou essa letra, pense em outra.')
      sleep(0.3)

    print('\n'+'=+'*20,'\n')
    
    amount_and_letter = [word.count(letter), letter]
    return amount_and_letter


  
  def desenha_forca(num):
    sleep(0.6)
  
    print("  _______     ")
    print(" |/      |    ")

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
        print(" |            ")

    if(num == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(num == 2):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |            ")
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
      mostra_palavra(word,right_letters)
      print('\nParabéns, você venceu!')
    else:
      print(f'A palavra era {word}.')
    print('\n'+'=+'*20)
  
 
  
  palavra = configura_palavra()
  qtde_letras_palavra = len(palavra)
  
  letras_certas = list()
  qtde_letras_certas = len(letras_certas)
  
  letras_erradas= list()
  
  tentativas = 6
  
  acertou = enforcou = False
  
  while (not acertou and not enforcou):
    sleep(0.3)

    print('Dica: fruta')
    
    mostra_palavra(palavra, letras_certas)
           
    mostra_letras_erradas(letras_erradas)
    
    qntd_letra_aparece_palavra = realiza_tentativa(letras_certas, letras_erradas, palavra)
    x_letra_aparece = qntd_letra_aparece_palavra[0]
    letra = qntd_letra_aparece_palavra[1]
    
    if (x_letra_aparece == 0):
      letras_erradas.append(letra)
      tentativas -= 1
      if(tentativas == 0):
        enforcou = True
    else:
      letras_certas.append(letra)
      qtde_letras_certas += palavra.count(letra)
      
      if (qtde_letras_certas == qtde_letras_palavra):
        print('Dica: fruta')
        acertou = True
      
    if(not acertou):
      desenha_forca(tentativas)
      
    sleep(0.3)
  
  finaliza(palavra, letras_certas)
  