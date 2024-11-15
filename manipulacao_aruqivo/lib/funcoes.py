#with open(nome_arquivo, objetivo de abrir o arquivo)
# 'r'-> lê coisa do arquivo, para arquivos simples, como: chave, senha, nome e etc. Para arquivos grandes, 'read lines', coisas no plural
# 'r+' -> é pra ler e escrever  
# 'w'-> escreve, Write, se não tiver um arquivo com o njome chamado, ele cria um e escreve oq vc falar pra ele SUBSTITUI
# 'a' -> ele adiviona uma informação.ADICIONA, prestar ateção no cursor. ou adicina um contra barra e n \n
#'enconding = utf-8' -> faz as letras sairem bonitas S2
# Esse 'as' faz com que o texto tenha um novo nome. Agora pra chamar ele é: arquivo.read() ou arquivo.readlines()

import csv

DATAPATH = 'manipulacao_aruqivo/db/mensagem.txt'
SAIDAPATH = 'manipulacao_aruqivo/db/saida.txt'
CSVPATH = 'manipulacao_aruqivo/db/tabela.csv'
CSVSAIDAPATH = 'manipulacao_aruqivo/db/saida.csv'


def total_palavras(): #1
    print('''Escreva um programa que leia um arquivo de texto e conte o número de palavras.''')
    with open(DATAPATH, 'r', encoding = 'utf-8') as bumbum:
        dados_bumbum = bumbum.read() #o read lê o arquivo todo como uma unica string, ent fica tudo junto e "misturado"
        bumbum_dividido = dados_bumbum.split()
        tamanho_bumbum = len(bumbum_dividido)
        print(tamanho_bumbum)


def contar_linhas(): #2
    print('''Desenvolva um algoritmo que leia um arquivo de texto e conte o número de linhas.''')
    with open(DATAPATH, 'r', encoding = 'utf-8') as bundoide: #nesse caso eu acredito que o enconding não seja necessario, já que as palavras não contam, só as linhas
        linhas_bundoides = bundoide.readlines()
    return len(linhas_bundoides)


def imprimir_texto_invertido(): #3
    print('''Faça um programa que leia um arquivo de texto e imprima o conteúdo invertido (da última linha para a primeira).''')
    with open(DATAPATH, 'r', encoding = 'utf-8') as bunda:
        texto_bundastico = bunda.readlines()
        for linha in texto_bundastico[::-1]:
            print(linha) #tem como fazer um return e texto[::-1] mas vai ficar meio porco, então vou utilizar um for pra deixar a mensagem mais clara e limpa.
        

def letra_inicial(): 
    print('''Escreva um programa que leia um arquivo de texto e imprima todas as palavras que começam com uma determinada letra''')
    with open (DATAPATH, 'r', encoding = 'utf-8') as busanfa:
        texto_da_busanfa = busanfa.read().lower() #tentei enfiar esse lower em um monte de lugar
        busanfa_separada = texto_da_busanfa.split()
        letra = str(input('Por favor, insira a letra inicial da palavra: ')).lower()
        for palavra in busanfa_separada:
            if letra in palavra[0]:
                print(palavra)
    return ''


def filtrar_linhas_por_palavra():
    print('''Desenvolva um algoritmo que leia um arquivo de texto e crie um novo arquivo apenas com as linhas que contêm um determinado palavra.''')

    palavra_filtrada = str(input('Insira a palavra que será filtrada: '))
    with open(DATAPATH, 'r', encoding='utf-8') as redondo_entrada:
        redondo_data = redondo_entrada.readlines() 

    with open(SAIDAPATH, 'w', encoding='utf-8') as redondo2_saida: #dava pra combinar o r e o w mas fiquei com medinho de embananar as coisas
        for linha in redondo_data:
            if palavra_filtrada in linha:
                redondo2_saida.write(linha)
    print(f"As linhas com a palavra '{palavra_filtrada}' foram salvas no arquivo {SAIDAPATH}.")


def imprimir_csv_como_tabela():
    print("Escreva um programa que leia um arquivo CSV e imprima o conteúdo na forma de uma tabela.")
    try:
        with open(CSVPATH, 'r', encoding = 'utf-8') as coxinha:
            leitor = csv.reader(coxinha)
            try:
                cabecalho = next(leitor)
                print(", ".join(cabecalho))
            except StopIteration:
                print("O arquivo CSV está vazio.")
                return

            for linha in leitor:
                print(", ".join(linha))

    except FileNotFoundError:
        print(f"Erro: O arquivo '{CSVPATH}' sumiu.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
print(imprimir_csv_como_tabela())



def calcular_media_coluna():
    print('''Crie um programa que leia um arquivo CSV e calcule a média dos valores de uma coluna específica.''')
    key = str(input('insira chave especifica: '))
    try:
        with open(CSVPATH, 'r', encoding = 'utf-8') as popozudo:
            leitor = csv.DictReader(popozudo)
            soma = 0
            contador = 0

            for linha in leitor:
                try:
                    valor = float(linha[key])
                    soma += valor
                    contador += 1
                except ValueError:
                    print(f"Valor inválido encontrado na linha: {linha}. Ignorando este valor.")
                except KeyError:
                    print(f"'{key}' não foi encontrada.")
                    return

            if contador == 0:
                print(f"Nenhum valor válido encontrado na coluna {key}.")
            else:
                media = soma / contador
                print(f"A média dos valores da coluna {key} é: {media:.2f}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def filtrar_csv():
    print('''Desenvolva um algoritmo que leia um arquivo CSV e crie um novo arquivo apenas com as linhas que atendem a um determinado critério.''')
    key_word = str(input('Insira o key_word de filtragem: '))
    with open(CSVPATH, 'r', encoding = 'utf-8') as traseiro:
        leitor = csv.DictReader(traseiro)

        with open(CSVSAIDAPATH, 'w', encoding = 'utf-8', newline = '') as traseiro_saida:
            escritor = csv.DictWriter(traseiro_saida, fieldnames = leitor.fieldnames)
            escritor.writeheader()

            for linha in leitor:
                if key_word(linha):
                    escritor.writerow(linha)


def combinar_arquivos():
    print('''Escreva um programa que leia dois arquivos de texto e crie um terceiro arquivo que seja a combinação dos dois primeiros.''')
    with open('txt+1arq.txt/db/mensagem.txt', 'r', encoding = 'utf-8') as coxinha1, \
         open(DATAPATH, 'r', encoding = 'utf-8') as coxinha2, \
         open(SAIDAPATH, 'w', encoding = 'utf-8') as coxinha_saida:

        coxinha_saida.write(coxinha1.read())
        coxinha_saida.write("Fins primeiro arquivo\n\n")
        coxinha_saida.write(coxinha2.read())


def binario_em_hexadecimal(caminho_arquivo):
    print('''Faça um programa que leia um arquivo binário e imprima o conteúdo em hexadecimal.''')
    with open(caminho_arquivo, 'rb') as bundinha:
        conteudo = bundinha.read()
        hex_output = ' '.join(f'{byte:02x}' for byte in conteudo)
        print(hex_output)
