from random import randint
from time import sleep
print('-'*25)
print('| Vamos jogar Jokenpo!! |')
print('|{:-^23}|' .format('Escolha'))
print('''| [ 0 ] Pedra           |
| [ 1 ] Papel           |
| [ 2 ] Tesoura         |''')
print('-'*25)
lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0 , 2)
J = int(input('Quantas vezes você irá jogar? '))
for c in range(0, J):
    jogador = int(input('Qual vai ser a sua jogada? '))
    if jogador not in (0, 1, 2):
        print('JOGUE UMA OPÇÃO VALIDA POR FAVOR!!!')
    else:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        sleep(1)
        print('=' * 29)
        print('Jogada do computador: {}'.format(lista[computador]))
        print('Jogada do Jogador: {}'.format(lista[jogador]))
        print('=' * 29)
        if computador == 0:  #computador jogou pedra
            if jogador ==0:
                print('Foi por pouco, você EMPATOU! :|')
            elif jogador ==1:
                print('Meus parabéns, você GANHOU!! :)')
            elif jogador ==2:
                print('Não foi dessa vez, você PERDEU! :(')
        elif computador ==1:  #computador jogou papel
            if jogador ==0:
                print('Não foi dessa vez, você PERDEU! :(')
            elif jogador ==1:
                print('Foi por pouco, você EMPATOU! :|')
            elif jogador ==2:
                print('Meus parabéns, você GANHOU!! :)')
        elif computador ==2:  #computador jogou tesoura
            if jogador ==0:
                print('Meus parabéns, você GANHOU!! :)')
            elif jogador ==1:
                print('Não foi dessa vez, você PERDEU! :(')
            elif jogador ==2:
                print('Foi por pouco, você EMPATOU! :|')
