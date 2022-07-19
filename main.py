import os
import random
import numpy as np

def adicionarplacar(ved):
    nomep1 = input('Digite o seu nome player 1:')
    nomep2 = input('Digite o seu nome player 2:')
    arquivo = open('placar.txt','r')
    placar = []
    for linha in arquivo:
        linha = linha.strip()
        placar.append(linha)
    x = placar.index('oi')
    print(x)

def Placar():
    arquivo = open('placar.txt','r')
    placar = []
    for linha in arquivo:
        linha = linha.strip()
        placar.append(linha)
    cont = 0
    for x in placar:
        print(x,'   ',end="")
        cont += 1
        if(cont == 3):
            cont = 0
            print('\n')

    arquivo.close

def P1VSCPU():
    jpp('CPU')
    telainicial()
def jpp(p1orp2):
    selecao = 'Sim'
    ved = [0,0]
    while selecao == 'Sim':
        if(p1orp2 == 'P1'):
            jogadap1 = selecaojogada('P1')
            jogadap2 = selecaojogada('P2')
            qg = quemganhou(jogadap1, jogadap2)
        elif(p1orp2 == 'CPU'):
            jogadap1 = selecaojogada('P1')
            jogadacpu = random.randint(1,4)
            if(jogadacpu == 1):
                jogadacpu = 'pedra'
            elif(jogadacpu == 2):
                jogadacpu = 'papel'
            else:
                jogadacpu = 'tesoura'

            qg = quemganhou(jogadap1, jogadacpu)
            if(qg == 2):
                cpuvenceu = 1
            else:
                cpuvenceu = 0
        else:
            jogadap1 = selecaojogada('P2')
            jogadap2 = selecaojogada('P1')
            qg = quemganhou(jogadap2, jogadap1) 
        if(p1orp2 == 'CPU'):
            print('CPU jogou',jogadacpu,'!')
            if(cpuvenceu == 1):
                print('CPU venceu!')
        if(qg == 1):
            print('Jogador 1 venceu!')
            ved[0] = ved[0] + 1
        elif(qg == 2):
            print('Jogador 2 venceu!')
            ved[1] = ved[1] + 1
        else:
            print('Empate!')
        selecao = input('Deseja jogar novamente? (Sim) (Nao):')
        while selecao != 'Sim' and selecao != 'Nao':
            os.system('clear')
            selecao = input('Deseja jogar novamente? (Sim) (Nao):')
    return ved
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
    ved = []
    if(jogarprimeiro == 'p1'):
        jp = 'p1'
    elif(jogarprimeiro == 'p2'):
        jp = 'p2'
    else:
        os.system('clear')
        P1VSP2()
    if(jp == 'p1'):
        ved = jpp('P1')        
    else:
        ved = jpp('P2')
    adicionarplacar(ved)
    telainicial()
def telaselecaomodo():
    os.system('clear')
    print('|                                                   |\n|               Pedra Papel e Tesoura               |\n|                   (1)-P1VSP2-                     |\n|                   (2)-P1VSCPU-                    |')
    selecao = input('Selecione uma Opção (1) (2):')
    if(selecao == '1'):
        P1VSP2()
    elif(selecao == '2'):
        P1VSCPU()
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
        Placar()
    elif(selecao == '3'):
        os.system('clear')
        pass
    else:
        os.system('clear')
        telainicial()

telainicial()