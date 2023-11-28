import os
from datetime import date
from time import sleep
from random import randrange

data = date.today().strftime('%d-%m-%Y')
nome_usuario = os.getlogin()

documentos_path = os.path.expanduser(f"C:\\Users\\{nome_usuario}\\Documents")
file_path = os.path.join(documentos_path, f'Pagamentos do dia {data}.txt')
total_path = os.path.join(documentos_path, f'Valores do dia {data}.txt')

def salvar_totais(total_dinheiro, total_pix, total_geral):
    with open(total_path, 'w') as arquivo:
        arquivo.write(f'Total em Dinheiro: {total_dinheiro:.2f}\n')
        arquivo.write(f'Total em Pix: {total_pix:.2f}\n')
        arquivo.write(f'Total Geral: {total_geral:.2f}')

def carregar_totais():
    if os.path.exists(total_path):
        with open(total_path, 'r') as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) >= 3:
                total_dinheiro = float(linhas[0].split(': ')[1])
                total_pix = float(linhas[1].split(': ')[1])
                total_geral = float(linhas[2].split(': ')[1])

                return total_dinheiro, total_pix
            
    return 0, 0

total_dinheiro, total_pix = carregar_totais()

if not os.path.exists(file_path):
    with open(file_path, 'w') as arquivo:
        arquivo.write('Cliente'.ljust(30) + " " +
                      'Mensalidade'.rjust(20) + " " +
                      'Pag. Adicional'.rjust(20) + " " +
                      ''.rjust(15) + "  " +
                      'Adicional'.ljust(30) + '\n')
        arquivo.write('-' * 150 + '\n')
    print(f'Arquivo criado em {file_path}')

class Programa:

    def __init__(self):
        self.total_dinheiro = total_dinheiro
        self.total_pix = total_pix
        self.total_geral = 0

    @staticmethod
    def limpar_tela():
        sistema = os.name
        if sistema == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    @staticmethod
    def obter_nome_valido():
        while True:
            nome = input('\nNome do Cliente (voltar 0): ').strip()
            if nome == '0':
                return 0
            nome_formatado = ' '.join(nome.split())
            if nome_formatado.replace(' ', '').isalpha():
                return nome_formatado.title()
            else:
                Programa.limpar_tela()
                print('Nome inválido. Por favor, insira apenas letras.')

    @staticmethod
    def pix_ou_dinheiro():
        while True:
            try:
                metodo_de_pagamento = int(input('''Qual o metodo de pagamento?
[1]Dinheiro      [2]PIX

Digite 1 ou 2: '''))

                if metodo_de_pagamento < 1 or metodo_de_pagamento > 2:
                    Programa.limpar_tela()
                    print('Valor inválido. Por favor digite o valor 1 ou 2')

                elif metodo_de_pagamento == 1:
                    metodo_de_pagamento = '(Dinheiro)'
                    return metodo_de_pagamento

                elif metodo_de_pagamento == 2:
                    metodo_de_pagamento = '(Pix)'
                    return metodo_de_pagamento

            except ValueError:
                Programa.limpar_tela()
                print('Valor inválido. Por favor digite o valor 1 ou 2')

    @staticmethod
    def obter_valor_pagamento_valido():
        while True:
            try:
                pagamento = float(input('\nValor Referente a Mensalidade: R$'))
                return pagamento
            except ValueError:
                Programa.limpar_tela()
                print('Valor de pagamento inválido. Por favor, insira apenas números.')

    @staticmethod
    def obter_valor_adicional_valido():
        while True:
            try:
                pagamento_adc = float(input('\nPagamento Adicional (digite 0 caso não tenha): R$'))
                return pagamento_adc
            except ValueError:
                Programa.limpar_tela()
                print('Valor adicional inválido. Por favor, insira um número válido.')

    def jogo_da_forca(self):
        if menu == 4:
            Programa.limpar_tela()
            if not os.path.exists('palavras.txt'):     
                sleep(0.5)
                print("Arquivo 'palavras.txt' não encontrado.")
                
                sleep(0.5)
                print('Criando Arquivo...')
                
                sleep(0.5)
                print('Arquivo criado com sucesso (caso queira adicionar novas palavras escreva uma abaixo da outra dentro do arquivo "palavras.txt)"\n')
                print('''assim:
                    palavra chave
                    palavra chave''')
                sleep(5)
            
            with open('palavras.txt', 'w'):
                pass
            print('\nInicianciando Jogo da Forca...')
            sleep(3)
            Programa.limpar_tela()


            arquivo = open('palavras.txt', 'r')

            print('*'*15)
            print('*Jogo da Forca*')
            print('*'*15)
            print()

                
            palavras = ['banana',
            'calice',
            'laranja',
            'paralelepipedo',
            'orangotango',
            'tangerina',
            'leao',
            'ferrari',
            'whinderssonnunes',
            'PNEUMOULTRAMICROSCOPICOSSILICOVULCANOCONIOSE',
            'batata',
            'jabuticaba',
            'escritorio',
            'ninja',
            'pitaia',
            'abacate',
            'lobisomen',
            'ametista',
            'luneta',
            'navio',
            'raquete',
            'arroz',
            'frango',
            'futebol',
            'gengibre',
            'washington',
            'malabarismo',
            'atlantida']
            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)

            if not palavras:
                sleep(2)
                print("O arquivo 'palavras.txt' está vazio, adicione algumas palavras e tente novamente.\n")
                sleep(1)
                exit()

            arquivo.close()

            palavra_aleatoria = randrange(0, len(palavras))

            palavra_secreta = palavras[palavra_aleatoria].upper()

            letras_corretas = ['_' for letra in palavra_secreta]
            letras = 0
            chances = 5

            dnv = 0

            while True:  
                
                palavra_aleatoria = randrange(0, len(palavras))
                palavra_secreta = palavras[palavra_aleatoria].upper()
                
                letras_corretas = ['_' for letra in palavra_secreta]
                letras = 0
                chances = 8
                
                print()
                print('Palavra: ',end='')
                print('_ ' * len(palavra_secreta))
                
                while True:  
                    
                    chute = str(input('\nDigite uma letra: ')).upper().strip()
                    print('\n')

                    for posi, letra in enumerate(palavra_secreta):
                        if chute == letra:
                            letras_corretas[posi] = letra
                    
                    if chute in palavra_secreta:
                        letras += 1
                        for pos in letras_corretas:
                            print(f'{pos} ',end='')
                    
                    if chute not in palavra_secreta:
                        chances -= 1
                        print(f'Não tem a letra ({chute})| Tentativas: {chances} ')
                        print("  _______     ")
                        print(" |/      |    ")

                        if chances == 7:
                            print(" |      (_)   ")
                            print(" |            ")
                            print(" |            ")
                            print(" |            ")

                        if chances == 6:
                            print(" |      (_)   ")
                            print(" |      \     ")
                            print(" |            ")
                            print(" |            ")

                        if chances == 5:
                            print(" |      (_)   ")
                            print(" |      \|    ")
                            print(" |            ")
                            print(" |            ")

                        if chances == 4:
                            print(" |      (_)   ")
                            print(" |      \|/   ")
                            print(" |            ")
                            print(" |            ")

                        if chances == 3:
                            print(" |      (_)   ")
                            print(" |      \|/   ")
                            print(" |       |    ")
                            print(" |            ")

                        if chances == 2:
                            print(" |      (_)   ")
                            print(" |      \|/   ")
                            print(" |       |    ")
                            print(" |      /     ")

                        if  chances == 1:
                            print(" |      (_)   ")
                            print(" |      \|/   ")
                            print(" |       |    ")
                            print(" |      / \   ")

                        print(" |            ")
                        print("_|___         ")
                        print()

                    if '_' not in letras_corretas:
                        print(": Parabéns, você ganhou!")
                        print("       ___________      ")
                        print("      '._==_==_=_.'     ")
                        print("      .-\\:      /-.    ")
                        print("     | (|:.     |) |    ")
                        print("      '-|:.     |-'     ")
                        print("        \\::.    /      ")
                        print("         '::. .'        ")
                        print("           ) (          ")
                        print("         _.' '._        ")
                        print("        '-------'       ")
                        break  
                    
                    if chances == 0:
                        print("Puxa, você foi enforcado!")
                        print(f"A palavra era {palavra_secreta}")
                        print("    _______________         ")
                        print("   /               \       ")
                        print("  /                 \      ")
                        print("//                   \/\  ")
                        print("\|   XXXX     XXXX   | /   ")
                        print(" |   XXXX     XXXX   |/     ")
                        print(" |   XXX       XXX   |      ")
                        print(" |                   |      ")
                        print(" \__      XXX      __/     ")
                        print("   |\     XXX     /|       ")
                        print("   | |           | |        ")
                        print("   | I I I I I I I |        ")
                        print("   |  I I I I I I  |        ")
                        print("   \_             _/       ")
                        print("     \_         _/         ")
                        print("       \_______/           ")
                        break  
                
                
                resposta = input("\nDeseja jogar novamente? (S/N) ").upper().strip()
                if resposta != "S":
                    Programa.limpar_tela()
                    sleep(0.5)
                    print('Saindo')
                    sleep(0.5)
                    print('.')
                    sleep(0.5)
                    print('.')
                    sleep(0.5)
                    print('.')
                    Programa.limpar_tela()
                    break
        
    def calcular_total_geral(self):
        total_geral = self.total_dinheiro + self.total_pix
        return total_geral

    def registrar_pagamento(self):
        while True:
            Programa.limpar_tela()
            print('=' * 30)
            print(f'{"Registrar Pagamentos":^30}')
            print('=' * 30)

            nome = Programa.obter_nome_valido()
            if nome == 0:
                Programa.limpar_tela()
                break

            metodo_pagamento = Programa.pix_ou_dinheiro()

            pagamento = Programa.obter_valor_pagamento_valido()

            pagamento_adc = Programa.obter_valor_adicional_valido()

            adicional = 'N/A'

            if metodo_pagamento == '(Dinheiro)':
                self.total_dinheiro += pagamento + pagamento_adc
            elif metodo_pagamento == '(Pix)':
                self.total_pix += pagamento + pagamento_adc

            #self.total_geral += self.total_dinheiro + self.total_pix

            if pagamento_adc >= 1:
                adicional = input('\nQual é o Adicional?: ').title()
            else:
                print('\nO Pagamento do Cliente Foi Registrado com Sucesso :)')

            cliente = Programa()
            linha = "{:<30} {:>20} {:>20} {:<17}{:<20}\n".format(
                nome,
                f'R${pagamento:.2f}'.replace('.', ','),
                f'R${pagamento_adc:.2f}'.replace('.', ','),
                f'{metodo_pagamento}',
                adicional)

            with open(file_path, 'a') as arquivo:
                arquivo.write(linha)

            salvar_totais(self.total_dinheiro, self.total_pix, self.calcular_total_geral())

            while True:
                Programa.limpar_tela()
                print('\nO Pagamento do Cliente Foi Registrado com Sucesso :)')

                voltar = str(input('\nContinuar Registrando Sim/Não: ')).upper().strip()
                Programa.limpar_tela()

                if voltar[0] == 'S':
                    Programa.limpar_tela()
                    break

                if voltar.isalpha():
                    return voltar.upper().strip()
                else:
                    Programa.limpar_tela()
                    print('Entrada inválida, Por favor, insira apenas Sim ou Não ou S ou N')

    def olhar_registro(self):
        Programa.limpar_tela()
        chato = 0
        while True:
            if os.path.exists(file_path):
                with open(file_path, "r") as arquivo:
                    conteudo = arquivo.read()
                    print(f'\n{conteudo}')
                    sair = str(input('Voltar Sim/Não: ')).upper()
                    Programa.limpar_tela()

                    if chato >= 2:
                        print('Ja te disse que não tem nada pra fazer aqui >:(')
                        sleep(2)
                        Programa.limpar_tela()
                        break

                    if sair[0] == 'S':
                        Programa.limpar_tela()
                        break

                    elif sair[0] == 'N' and chato <= 2:
                        chato += 1
                        print("Não tem outra coisa pra fazer por aqui '-' ")
                        sleep(2)
                        Programa.limpar_tela()
            else:
                print("O arquivo de registro não existe.")
                break

    def fechar_caixa(self):
        Programa.limpar_tela()
        print('=' * 30)
        print(f'{"Fechar Caixa":^30}')
        print('=' * 30)
        print(f'Total em Dinheiro: R${self.total_dinheiro:.2f}')
        print(f'Total em Pix: R${self.total_pix:.2f}')
        print(f'Total Geral: R${self.calcular_total_geral():.2f}')
        print('=' * 30)


    def fechar(self):
        salvar_totais(self.total_dinheiro, self.total_pix, self.total_geral)
        sleep(0.5)
        Programa.limpar_tela()
        print('Finalizando Programa...')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print('.')
        print('Programa Finalizado :)')
        exit()

    def opcao_invalida(self):
        Programa.limpar_tela()
        print(f'O número {menu} não existe no menu! Tente outro!')
        sleep(2)
        Programa.limpar_tela()

programa = Programa()

while True:
    try:
        menu = int(input('''
[1] Registrar Pagamento De Clientes
[2] Olhar Registros de Pagamento
[3] Fechar Caixa
[0] Fechar Aplicativo

Digite o número de uma das opções acima: '''))

        if menu == 1:
            programa.registrar_pagamento()
        elif menu == 2:
            programa.olhar_registro()
        elif menu == 3:
            programa.fechar_caixa()
        elif menu == 0:
            programa.fechar()
        elif menu == 4:
            programa.jogo_da_forca()
        else:
            programa.opcao_invalida()

    except ValueError:
        Programa.limpar_tela()
        print(f'\nErro, Digite um número válido que seja entre 0 e 4\n')
        sleep(1)
        Programa.limpar_tela()
