import os

def jpp(p1orp2):
    selecao = 'Sim'
    while selecao == 'Sim':
        if(p1orp2 == 'P1'):
            jogadap1 = selecaojogada('P1')
            jogadap2 = selecaojogada('P2')
            qg = quemganhou(jogadap1, jogadap2)
        else:
            jogadap1 = selecaojogada('P2')
            jogadap2 = selecaojogada('P1')
            qg = quemganhou(jogadap2, jogadap1)       
        if(qg == 1):
            print('Jogador 1 venceu!')
        elif(qg == 2):
            print('Jogador 2 venceu!')
        else:
            print('Empate!')
        selecao = input('Deseja jogar novamente? (Sim) (Nao):')
        while selecao != 'Sim' and selecao != 'Nao':
            os.system('clear')
            selecao = input('Deseja jogar novamente? (Sim) (Nao):')
        
def selecaojogada(p1orp2):
    os.system('clear')
    print('|                                                   |\n|            Jogador',p1orp2,'escolha sua jogada          |\n|                   (1)-Pedra-                      |\n|                   (2)-Papel-                      |\n|                   (3)-Tesoura-                    |')
    selecao = input('Selecione uma Opção (1) (2) (3):')
    if(selecao == '1'):
        return 'pedra'
    elif(selecao == '2'):
        return 'papel'
    elif(selecao == '3'):
        return 'tesoura'
    else:
        selecaojogada()

def quemganhou(jogadap1,jogadap2):
    if(jogadap1 == 'pedra'):
        if(jogadap2 == 'pedra'):
            return 3
        elif(jogadap2 == 'papel'):
            return 2
        elif(jogadap2 == 'tesoura'):
            return 1
    elif(jogadap1 == 'papel'):
        if(jogadap2 == 'pedra'):
            return 2
        elif(jogadap2 == 'papel'):
            return 3
        elif(jogadap2 == 'tesoura'):
            return 1
    elif(jogadap1 == 'tesoura'):
        if(jogadap2 == 'pedra'):
            return 2
        elif(jogadap2 == 'papel'):
            return 1
        elif(jogadap2 == 'tesoura'):
            return 3      
     
def P1VSP2():
    jogarprimeiro = input('Qual jogador jogará primeiro? (p1) (p2):')
    if(jogarprimeiro == 'p1'):
        jp = 'p1'
    elif(jogarprimeiro == 'p2'):
        jp = 'p2'
    else:
        os.system('clear')
        P1VSP2()

    if(jp == 'p1'):
        jpp('P1')        
    else:
        jpp('P2')

    telainicial()
def telaselecaomodo():
    os.system('clear')
    print('|                                                   |\n|               Pedra Papel e Tesoura               |\n|                   (1)-P1VSP2-                     |\n|                   (2)-P1VSCPU-                    |')
    selecao = input('Selecione uma Opção (1) (2):')
    if(selecao == '1'):
        P1VSP2()
    elif(selecao == '2'):
        pass
    else:
        os.system('clear')
        telaselecaomodo()

def telainicial():
    os.system('clear')
    print('|                                                   |\n|               Pedra Papel e Tesoura               |\n|                   (1)-Jogar-                      |\n|                   (2)-Placar-                     |\n|                   (3)-Sair-                       |')
    selecao = input('Selecione uma Opção (1) (2) (3):')
    if(selecao == '1'):
        telaselecaomodo()
    elif(selecao == '2'):
        pass
    elif(selecao == '3'):
        os.system('clear')
        pass
    else:
        os.system('clear')
        telainicial()

telainicial()