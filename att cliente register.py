import os
from datetime import date
from time import sleep
from random import randrange

data = date.today().strftime('%d-%m-%Y')
nome_usuario = os.getlogin()

documentos_path = os.path.expanduser(f"C:\\Users\\{nome_usuario}\\Documents")
file_path = os.path.join(documentos_path, f'Registros dos Clientes {data}.txt')
total_path = os.path.join(documentos_path, f'Dinheiro do Caixa {data}.txt')
detalhes_path = os.path.join(documentos_path, f'Detalhes do Caixa {data}.txt')

def salvar_totais(total_dinheiro, total_pix, total_deposito, total_geral,
                total_retirado):
    with open(total_path, 'w') as arquivo:
        arquivo.write('='*35)
        arquivo.write('\n')
        arquivo.write(f'Total em Dinheiro: R${total_dinheiro:.2f}\n'.replace('.',','))
        arquivo.write(f'Total em Pix: R${total_pix:.2f}\n'.replace('.',','))
        arquivo.write(f'Total em Depósito: R${total_deposito:.2f}\n'.replace('.',','))
        arquivo.write(f'Total Geral: R${total_geral:.2f}\n'.replace('.',','))
        arquivo.write(f'Valor Retirado do Caixa: R${total_retirado:.2f}'.replace('.',','))
        arquivo.write('\n')
        arquivo.write('='*35)

if not os.path.exists(detalhes_path):
    with open(detalhes_path, 'w') as arquivo:
        arquivo.write('Motivo'.ljust(40) + 'Valor'.ljust(20) + 'Quem'.ljust(25) + '\n')
        arquivo.write('-' * 65 + '\n')



def carregar_totais():
    if os.path.exists(total_path):
        with open(total_path, 'r') as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) >= 6:
                total_dinheiro = float(linhas[1].split(': ')[1].replace('R$', '').replace(',', '').replace('\n', ''))
                total_pix = float(linhas[2].split(': ')[1].replace('R$', '').replace(',', '').replace('\n', ''))
                total_deposito = float(linhas[3].split(': ')[1].replace('R$', '').replace(',', '').replace('\n', ''))
                total_retirado_str = linhas[5].split(': ')[1].replace('R$', '').replace(',', '').replace('\n', '')
                total_retirado = float(total_retirado_str) if total_retirado_str[0] != '-' else -float(total_retirado_str[1:])
                return total_dinheiro, total_pix, total_deposito, total_retirado

            elif len(linhas) == 4:
                total_dinheiro = float(linhas[0].split(': ')[1].replace('R$', '').replace(',', '').replace('\n', ''))
                total_pix = float(linhas[1].split(': ')[1].replace('R$', '').replace(',', '').replace('\n', ''))
                return total_dinheiro, total_pix, 0, 0
            
    return 0, 0, 0, 0

total_dinheiro, total_pix, total_deposito, total_retirado = carregar_totais()


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
        self.total_deposito = total_deposito
        self.total_geral = 0
        self.total_retirado = total_retirado
        self.valor_a_remover = 0
        self.quem = ''
        self.motivo = ''

    @staticmethod
    def limpar_tela():
        sistema = os.name
        if sistema == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    
    #@staticmethod
    def remover_valor_caixa(self):
        while True:
            Programa.limpar_tela()
            sair = False
            try:
                total_dinheiro, total_pix, total_deposito, total_retirado = self.total_dinheiro, self.total_pix, self.total_deposito, self.total_retirado
                print('='*35)
                print(f'{"Retirar Dinheiro":^35}')
                print('='*35)

                valor_a_remover_str = input('Quanto deseja retirar do caixa? (Digite 0 para voltar): R$')
                valor_a_remover_str = valor_a_remover_str.replace(',','.')
                
                self.valor_a_remover = float(valor_a_remover_str)
                

                if self.valor_a_remover > total_dinheiro:
                    Programa.limpar_tela()
                    print('O valor a ser retirado é maior que o disponível')            
                    return
                    
                elif self.valor_a_remover == 0:
                    Programa.limpar_tela()
                    break
                
                Programa.limpar_tela()
                print(f'Retirando R${self.valor_a_remover:.2f}'.replace('.',','))

                self.total_dinheiro -= self.valor_a_remover

                self.total_retirado += self.valor_a_remover
                
                
                while True:
                    try:
                        motivo = int(input('''\nMotivo:
[1] Abastecimento    [2] Outros   [3] voltar 
                                    
Digite 1, 2 ou 3: '''))

                        if motivo == 1:
                            motivo = "Abastecimento"
                            
                            sair = True
                            self.quem = input('Quem Abasteceu: ').title()
                            
                            
                            
                            Programa.limpar_tela()
                            print(f'R${self.valor_a_remover:.2f} Retirado do Caixa'.replace('.',','))

                            salvar_totais(
                                self.total_dinheiro, self.total_pix, self.total_deposito,
                                self.total_geral + self.total_dinheiro + self.total_pix + self.total_deposito,
                                self.total_retirado)        
                        
                            with open(detalhes_path, 'a') as arquivo:
                                arquivo.write(f'{motivo}'.ljust(40) + f'{self.valor_a_remover:.2f}'.replace('.',',').ljust(20) + f'{self.quem}'.ljust(25) + '\n')
                            
                            break
                        
                        elif motivo == 2:
                            motivo = "Outros"
                            
                            sair = True
                            self.motivo = input('Escreva o Motivo: ').title()
                            
                            quem = input(f'Quem Está Retirando: ').replace('.',',')
                            
                            
                            Programa.limpar_tela()
                            print(f'R${self.valor_a_remover:.2f} Retirado do Caixa'.replace('.',','))

                            salvar_totais(
                                self.total_dinheiro, self.total_pix, self.total_deposito,
                                self.total_geral + self.total_dinheiro + self.total_pix + self.total_deposito,
                                self.total_retirado)    

                            with open(detalhes_path, 'a') as arquivo:
                                arquivo.write(f'{self.motivo}'.ljust(40) + f'{self.valor_a_remover:.2f}'.replace('.',',').ljust(20) + f'{quem}'.ljust(25) + '\n')
                            break
                        
                        elif motivo == 3:
                            break
                            
                    

                    except ValueError:
                        Programa.limpar_tela()
                        print('Valor Inválido, Digite Apenas Números')
                        continue

                    
                    
            except ValueError:
                Programa.limpar_tela()
                print('Valor Inválido, Digite Apenas Números')

            if sair:
                break



    @staticmethod
    def obter_nome_valido():
        while True:
            nome = input('\nNome do Cliente (Para Voltar Digite 0): ').strip()
            if nome == '0':
                return 0
            nome_formatado = ' '.join(nome.split())
            if nome_formatado.replace(' ', '').isalpha() or '(' in nome_formatado or ')' in nome_formatado:
                return nome_formatado.title()
            else:
                Programa.limpar_tela()
                print('Nome inválido. Por favor, insira apenas letras.')

    @staticmethod
    def pix_ou_dinheiro():
        while True:
            try:
                metodo_de_pagamento = int(input('''Qual o metodo de pagamento?
[1]Dinheiro      [2]PIX     [3]Depósito     [0]Voltar

Digite 1, 2 ou 3: '''))

                if metodo_de_pagamento < 0 or metodo_de_pagamento > 3:
                    Programa.limpar_tela()
                    print('Valor inválido. Por favor digite o valor 1, 2 ou 3')

                elif metodo_de_pagamento == 0:
                    return 0

                elif metodo_de_pagamento == 1:
                    metodo_de_pagamento = '(Dinheiro)'
                    return metodo_de_pagamento

                elif metodo_de_pagamento == 2:
                    metodo_de_pagamento = '(Pix)'
                    return metodo_de_pagamento
                
                elif metodo_de_pagamento == 3:
                    metodo_de_pagamento = '(Depósito)'
                    return metodo_de_pagamento

            except ValueError:
                Programa.limpar_tela()
                print('Valor inválido. Por favor digite o valor 1, 2 ou 3')

    @staticmethod
    def obter_valor_pagamento_valido():
        while True:
            try:
                pagamento_str = input('\nValor da Mensalidade (Para Voltar Digite 0): R$')
                pagamento_str = pagamento_str.replace(',','.')

                pagamento = float(pagamento_str)

                return pagamento
            
            except ValueError:
                Programa.limpar_tela()
                print('Valor de pagamento inválido. Por favor, insira apenas números.')

    @staticmethod
    def obter_valor_adicional_valido():
        while True:
            try:
                pagamento_adc_str = input('\nPagamento Adicional (digite 0 caso não tenha): R$')
                pagamento_adc_str = pagamento_adc_str.replace(',', '.')

                pagamento_adc = float(pagamento_adc_str)

                return pagamento_adc
            except ValueError:
                Programa.limpar_tela()
                print('Valor adicional inválido. Por favor, insira apenas números.')

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
        
    

    def registrar_pagamento(self):
        while True:
            Programa.limpar_tela()
            print('=' * 30)
            print(f'{"Registrar Pagamentos":^30}')
            print('=' * 30)

            nome = self.obter_nome_valido()
            if nome == 0:
                Programa.limpar_tela()
                break

            metodo_pagamento = self.pix_ou_dinheiro()
            if metodo_pagamento == 0:
                Programa.limpar_tela()
                self.registrar_pagamento()
                break

            pagamento = self.obter_valor_pagamento_valido()
            if pagamento == 0:
                Programa.limpar_tela()
                self.registrar_pagamento()


            pagamento_adc = self.obter_valor_adicional_valido()

            adicional = 'N/A'

            if metodo_pagamento == '(Dinheiro)':
                self.total_dinheiro += pagamento + pagamento_adc
            
            elif metodo_pagamento == '(Pix)':
                self.total_pix += pagamento + pagamento_adc

            elif metodo_pagamento == '(Depósito)':
                self.total_deposito += pagamento + pagamento_adc
            

            

            if pagamento_adc >= 1:
                while True:
                    adicional = input('\nQual é o Adicional?: ').title()
                    if adicional != '':
                        break

                    else:
                        print('Esse Espaço Não Pode Ficar em Branco, Digite algo.')
            else:
                print('\nO Pagamento do Cliente Foi Registrado com Sucesso :)')

            programa = Programa()
            linha = "{:<30} {:>20} {:>20} {:<17}{:<20}\n".format(
                nome,
                f'R${pagamento:.2f}'.replace('.', ','),
                f'R${pagamento_adc:.2f}'.replace('.', ','),
                f'{metodo_pagamento}',
                adicional)

            with open(file_path, 'a') as arquivo:
                arquivo.write(linha)

            salvar_totais(self.total_dinheiro, self.total_pix, self.total_deposito,
                         self.total_geral + self.total_dinheiro + self.total_pix + self.total_deposito,
                         self.total_retirado)

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
                    print('Entrada inválida, Por favor, insira apenas Sim ou Não / ou S ou N')

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
                        print('Que Curioso(a) em')
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
        print('=' * 35)
        print(f'{"Fechar Caixa":^35}')
        if os.path.exists(total_path):
                with open(total_path, "r") as arquivo:
                    conteudo = arquivo.read()
                    print(f'{conteudo}'.replace('.',','))
                    print('\n\n')
                
                with open(detalhes_path, 'r') as arquiv:
                    cont = arquiv.read()
                    print(f'{cont}'.replace('.',','))


    def fechar(self):
        salvar_totais(self.total_dinheiro, self.total_pix, self.total_deposito, self.total_geral + self.total_dinheiro + self.total_pix + self.total_deposito, self.total_retirado)
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
        print(f'O número {menu} não existe no menu! Digite um Número entre 0 e 4!')
        sleep(2)
        Programa.limpar_tela()

programa = Programa()

while True:
    try:
        
        menu = int(input('''
[1] Registrar Pagamento De Clientes
[2] Olhar Registros de Clientes
[3] Fechar Caixa
[4] Retirar Dinheiro do Caixa
[0] Fechar Programa

Digite o número de uma das opções acima: '''))

        if menu == 1:
            programa.registrar_pagamento()
        elif menu == 2:
            programa.olhar_registro()
        elif menu == 3:
            Programa.limpar_tela()
            programa.fechar_caixa()
        elif menu == 4:
            programa.remover_valor_caixa()
        elif menu == 5:
            programa.jogo_da_forca()
        elif menu == 0:
            programa.fechar()
        else:
            programa.opcao_invalida()

    except ValueError:
        Programa.limpar_tela()
        print(f'\nErro, Digite um número válido que seja entre 0 e 4\n')
        sleep(1)
        Programa.limpar_tela()
