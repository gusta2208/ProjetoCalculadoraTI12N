import this

import multiplicacao
import soma
import subtracao
import divisao
import tabuada
import vetores
this.opcao = 0 #crio a variável global
num1 = 0
num2 = 0

def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input())

def coletarNum2():
    print('Informe o segundo número: ')
    this.num2 = float(input())

def mostrarMenu():
    print('Escolha uma das opções abaixo: ' +
          '\n1. Soma' +
          '\n2. Subtração' +
          '\n3. Multiplicação' +
          '\n4. Divisão' +
          '\n5. Tabuada' +
          '\n6. Vetor' +
          '\n0. Sair')
    this.opcao = int(input()) #coletar a digitação do usuario


def operecao():
    #Mostrar o menu em tela
    while this.opcao != 5:
        mostrarMenu()
        #realizar as operações
        if this.opcao == 1:
            coletarNum1()
            coletarNum2()
            print(soma.somar(this.num1, this.num2))
        elif this.opcao == 2:
            #Operação para subtrair
            coletarNum1()
            coletarNum2()
            print(subtracao.subtrair(this.num1, this.num2))
        elif this.opcao == 3:
            #Operação multiplicar
            coletarNum1()
            coletarNum2()
            print(multiplicacao.multiplicar(this.num1, this.num2))
        elif this.opcao == 4:
            #Operação dividir
            coletarNum1()
            coletarNum2()
            print(divisao.dividir(this.num1, this.num2))
        elif this.opcao == 5:
            coletarNum1()
            coletarNum2()
            print(tabuada.calcularTabuada(int(this.num1), int(this.num2)))
        elif this.opcao == 6:
            vetores.mostrarVetor()
        elif this.opcap == 0:
            print('Obrigado!')
        else:
            print('Opção escolhida invlálida, tente novamente!')