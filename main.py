import adivinhacao
import forca

print("""O que você quer jogar?\n 
1 ---- Adivinhação
2 ---- Forca\n""")

opcao = 0
while (opcao != 1 and opcao != 2):
  opcao =input('Sua escolha [1 / 2]: ').strip()
  if(opcao == '1' or opcao == '2'):
    break
  print('Escolha corretamente.',end=' ')

if (opcao == '1'):
  print('Você escolheu o jogo de adivinhação. Vamos lá.\n')
  print('=+'*32,'\n')
  adivinhacao.jogar()
else:
  print('Você escolheu o jogo da forca. Vamos lá.\n')
  print('=+'*32,'\n')
  forca.jogar()
