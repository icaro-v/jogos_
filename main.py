import adivinhacao
import forca

print("""O que você quer jogar?\n 
1 ---- Adivinhação
2 ---- Forca\n""")

jogo = ["de adivinhação", "da forca"]

while True:
  opcao =input('Sua escolha [1 / 2]: ').strip()
  if(opcao == '1' or opcao == '2'):
    opcao = int(opcao)-1
    break
  print('Escolha corretamente.',end=' ')


print(f'\nVocê escolheu o jogo {jogo[opcao]}. Vamos lá.\n')
print('=+'*32,'\n')
adivinhacao.jogar() if (opcao == 0) else forca.jogar()
