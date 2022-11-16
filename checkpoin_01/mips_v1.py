'''
Objetivos:
- Ler o arquivo binário já feito previamente
- Identificar os tipos de operações
- 'Fazer' os registradores
- Executar as operações
- Achar algum jeito simples de mostrar o estado dos registradores
'''
#---------------------Modo de funcionamento---------------------
'''
    Definição dos registradores:
    regs = {'simbolo' : [simbolo do reg], 'cod' : [código do reg], 'conteudo' : [conteudo do reg]}
    temporarios:
        simbolo     cod
        $t0         0001
        $t1         0010
        $t2         0011
    salvos:
        simbolo     cod
        $s0         0111
        $s1         1000
        $s2         1001
        $s3         1010
        $s4         1011
    ***Por definição o conteúdo de todos os registradores já vem com o valor 0000    

    Operações:
        tipo        cod
        li          1011
        add         0010
        sub         0011
'''
#Bibliotecas
import pickle
from sum_sub import sum, sub

#---------------------Funções---------------------

#Função que trata o arquivo, convertendo o arquivo texto
# para binario e armazenando o texto do arquivo em binario
# novamente
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

#Função que identifica e exclui os comentarios do arquivo texto
def comentarios(linhas):
    #Desconsiderando os comentarios
    count = 0
    aux = 0
    while count < (len(linhas)):
        letra = linhas[count][aux]
        if letra == '#':
            del(linhas[count])
        count += 1

#Função que identifica que tipo de função que é e a amazena 
# no dicionario
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

#Identificação e execução das instruções
def executa(linhas, regs):
    for count in range(0, len(linhas)):
        cont_linha = linhas[count].split(' ')
        count = 0
        if len(cont_linha) == 3:
            if cont_linha[0] == '1011':
                while True:
                    if cont_linha[1] == regs[count]['cod']:
                        regs[count]['conteudo'] = cont_linha[2]
                        break
                    else:
                        count += 1
        if len(cont_linha) == 4:
            count = 0
            while True:
                if cont_linha[2] == regs[count]['cod']:
                    num1 = regs[count]['conteudo']
                if cont_linha[3] == regs[count]['cod']:
                    num2 = regs[count]['conteudo']
                    break
                else:
                    count += 1
            if cont_linha[0] == '0010':
                res = sum(num1, num2)
            if cont_linha[0] == '0011':
                res = sub(num1, num2)
            count = 0
            while True:
                if cont_linha[1] == regs[count]['cod']:
                    regs[count]['conteudo'] = res
                    break
                else:
                    count += 1                    


        

#Define e inicia os registradores com 0000 em conteudo
def inicia_reg(reg, regs):
    reg = {'simbolo' : '$t0', 'cod' : '0001', 'conteudo' : '0000'}
    regs.append(reg)
    reg = {'simbolo' : '$t1', 'cod' : '0010', 'conteudo' : '0000'}
    regs.append(reg)
    reg = {'simbolo' : '$t2', 'cod' : '0011', 'conteudo' : '0000'}
    regs.append(reg)
    reg = {'simbolo' : '$s0', 'cod' : '0111', 'conteudo' : '0000'}
    regs.append(reg)
    reg = {'simbolo' : '$s1', 'cod' : '1000', 'conteudo' : '0000'}
    regs.append(reg)
    reg = {'simbolo' : '$s2', 'cod' : '1001', 'conteudo' : '0000'}
    regs.append(reg)
    reg = {'simbolo' : '$s3', 'cod' : '1010', 'conteudo' : '0000'}
    regs.append(reg)
    reg = {'simbolo' : '$s4', 'cod' : '1011', 'conteudo' : '0000'}
    regs.append(reg)
       
#---------------------Main---------------------
if __name__ == '__main__':
    conteudo = tratamento_arquivo('teste.b', 'teste.txt')

    #Armazenando as linhas
    linhas = conteudo.split('\n')

    #Chamando a função que desconsidera os comentarios
    comentarios(linhas)

    linhas_li, linhas_arit = armazena_instrucoes(linhas)
    
    #Definindo o dicionario registradores e a lista de registradores
    reg = {}
    regs = []
    inicia_reg(reg, regs)
    executa(linhas, regs)
    for count in range(0, len(regs)):
        registrador = regs[count]['simbolo']
        conteudo = regs[count]['conteudo']
        print(f'Registrador: {registrador}  Conteudo: {conteudo}')
    
    
