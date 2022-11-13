'''
Objetivos:
- Ler o arquivo binário já feito previamente
- Identificar os tipos de operações
- 'Fazer' os registradores
- Executar as operações
- Achar algum jeito simples de mostrar o estado dos registradores
'''
#Bibliotecas
import pickle

#Funções
def tratamento_arquivo(arquivo_bin, arquivo_txt):
    #Lendo o arquivo texto para transforma-lo em binario para depois
    #transforma-lo em texto (temporário)
    arquivo = open(arquivo_txt, 'r')
    texto = arquivo.read()
    arquivo.close()

    #Armazenando o conteudo do arquivo texto em um arquivo binario(temporario)
    try: 
        arquivo = open(arquivo_bin, 'wb')
        pickle.dump(texto, arquivo)
        arquivo.close()
    except:
        print('Erro na escrita no arquivo binario!!')

    #Lendo o conteudo do arquivo binario e o armazenando em uma variavel
    try:
        arquivo = open(arquivo_bin, 'rb')
        conteudo = pickle.load(arquivo)
        arquivo.close()
    except:
        print('Erro ao ler o arquivo binario!!')
    
    return conteudo

def comentarios(linhas):
    #Desconsiderando os comentarios
    count = 0
    aux = 0
    while count < (len(linhas)):
        letra = linhas[count][aux]
        if letra == '#':
            del(linhas[count])
        count += 1
    print(linhas)

def armazena_instrucoes(linhas):
    instrucoes_li = {}
    instrucoes_arit = {}
    linhas_li = []
    linhas_arit = []
    count = 0
    
    while count < len(linhas):
        conteudo_linhas = linhas[count].split()
        if len(conteudo_linhas) == 3:
            instrucoes_li['operation'] = conteudo_linhas[0]
            instrucoes_li['regD'] = conteudo_linhas[1]
            instrucoes_li['const'] = conteudo_linhas[2]
            linhas_li.append(instrucoes_li)
        if len(conteudo_linhas) == 4:
            instrucoes_arit['operation'] = conteudo_linhas[0]
            instrucoes_arit['regD'] = conteudo_linhas[1]
            instrucoes_arit['reg1'] = conteudo_linhas[2]
            instrucoes_arit['reg2'] = conteudo_linhas[3]
            linhas_arit.append(instrucoes_arit)
        count += 1
    
    return linhas_li, linhas_arit


            

if __name__ == '__main__':
    conteudo = tratamento_arquivo('teste.b', 'teste.txt')

    #Armazenando as linhas
    linhas = conteudo.split('\n')

    #Chamando a função que desconsidera os comentarios
    comentarios(linhas)

    linhas_li, linhas_arit = armazena_instrucoes(linhas)

    print(linhas_li[0])
    print(len(linhas_li))
    print(len(linhas_arit))

    
