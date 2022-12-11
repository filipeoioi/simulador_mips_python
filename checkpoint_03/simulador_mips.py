def carregarInstrucoes(arquivoEntrada, instrucoes):
    for linha in arquivoEntrada:
        if '#' not in linha: 
            linha = linha.replace('\n', '')
            instrucoes.append([linha[y-4:y] for y in range(4, len(linha)+4,4)])

def recebeRegistro(a, t, s, cod):
    if cod == '0001': return t[0]
    elif cod == '0010': return t[1]
    elif cod == '0011': return t[2]
    elif cod == '0100': return a[0]
    elif cod == '0101': return a[1]
    elif cod == '0110': return a[2]
    elif cod == '0111': return s[0]
    elif cod == '1000': return s[1]
    elif cod == '1001': return s[2]
    elif cod == '1010': return s[3]
    elif cod == '1011': return s[4]

def modificaRegistrador(a, t, s, cod, n):
    if cod == '0001': t[0] = n
    elif cod == '0010': t[1] = n
    elif cod == '0011': t[2] = n
    elif cod == '0100': a[0] = n
    elif cod == '0101': a[1] = n
    elif cod == '0110': a[2] = n
    elif cod == '0111': s[0] = n
    elif cod == '1000': s[1] = n
    elif cod == '1001': s[2] = n
    elif cod == '1010': s[3] = n
    elif cod == '1011': s[4] = n

def somaRegistrador(a, t, s, cod, n):
    if cod == '0001': t[0] += n
    elif cod == '0010': t[1] += n
    elif cod == '0011': t[2] += n
    elif cod == '0100': a[0] += n
    elif cod == '0101': a[1] += n
    elif cod == '0110': a[2] += n
    elif cod == '0111': s[0] += n
    elif cod == '1000': s[1] += n
    elif cod == '1001': s[2] += n
    elif cod == '1010': s[3] += n
    elif cod == '1011': s[4] += n

def executaInstrucaoJ(instrucao, a, t, s, pc, ra):
    if instrucao[0] == '1010':
        p = str(bin(recebeRegistro(a, t, s, instrucao[1]))).replace('b', '')

        binarios = list(p)

        for i in range(len(binarios)):
            if binarios[i] == '0':
                binarios[i] = '1'
            else:
                binarios[i] = '0'
        
        join = ''.join(binarios)
        decimal = int(join, 2)

        modificaRegistrador(a, t, s, instrucao[1], decimal)

        #print(f'inverteu o valor do registrador {instrucao[1]}')

        pc[0] += 4

    if instrucao[0] == '1110':
        ins = instrucao[2] + instrucao[3]
        #print(f"Jumpando para {int(ins, 2) * 4}")
        pc[0] = int(ins, 2) * 4

    if instrucao[0] == '1111':
        ins = instrucao[2] + instrucao[3]
        #print(f"Jumpando para {int(ins, 2) * 4}")
        ra[0] = pc[0]
        pc[0] = int(ins, 2) * 4
        return
          
def executaInstrucaoI(instrucao, a, t, s, pc):
    if instrucao[0] == '1000':
        numeroDecimal = int(instrucao[3], 2)
        somaRegistrador(a, t, s, instrucao[2], numeroDecimal)
        #print(f'somando {numeroDecimal} em {instrucao[2]}')
        pc[0] += 4

    if instrucao[0] == '1001':
        p = str(bin(recebeRegistro(a, t, s, instrucao[1]))).replace('b', '')
        binario = p[1:]

        binarios = list(binario)
        for i in range(int(instrucao[3], 2)):
            binarios = binarios[-1:] + binarios[:-1]

        join = ''.join(binarios)
        decimal = int(join, 2)

        modificaRegistrador(a, t, s, instrucao[2], decimal)

        #print(f'shiftando o registro {binario} para {"".join(binarios)} e salvando em {instrucao[2]} ')
        pc[0] += 4

    if instrucao[0] == '1100':
        if recebeRegistro(a, t, s, instrucao[1]) == recebeRegistro(a, t, s, instrucao[2]):
            pc[0] = int(instrucao[3], 2) * 4
            #print("Comparacao sucesso")
            return
        #print("Comparacao falhou")
        pc[0] += 4

    if instrucao[0] == '1101':
        if recebeRegistro(a, t, s, instrucao[1]) < recebeRegistro(a, t, s, instrucao[2]):
            pc[0] = int(instrucao[3], 2) * 4
            #print("Comparacao sucesso")
            return
        #print("Comparacao falhou")
        pc[0] += 4
def executaInstrucaoR(instrucao, a, t, s, pc):
    aux = 0

    if instrucao[0] == '0010':
        #print(f'{recebeRegistro(a, t, s, instrucao[1])} + {recebeRegistro(a, t, s, instrucao[2])}')
        modificaRegistrador(a, t, s, instrucao[3], (recebeRegistro(a, t, s, instrucao[1]) + recebeRegistro(a, t, s, instrucao[2])))    
        pc[0] += 4
    
    if instrucao[0] == '0011':
        #print(f'{recebeRegistro(a, t, s, instrucao[1])} - {recebeRegistro(a, t, s, instrucao[2])}')
        modificaRegistrador(a, t, s, instrucao[3], (recebeRegistro(a, t, s, instrucao[1]) - recebeRegistro(a, t, s, instrucao[2])))        
        pc[0] += 4

    if instrucao[0] == '0100':
        #print(f'{recebeRegistro(a, t, s, instrucao[1])} and {recebeRegistro(a, t, s, instrucao[2])} = 1?')
        if recebeRegistro(a, t, s, instrucao[1]) == recebeRegistro(a, t, s, instrucao[2]) == 1:
            aux = 1
        modificaRegistrador(a, t, s, instrucao[3], aux)        
        pc[0] += 4

    if instrucao[0] == '0101':
        #print(f'{recebeRegistro(a, t, s, instrucao[1])} or {recebeRegistro(a, t, s, instrucao[2])} = 1?')
        if recebeRegistro(a, t, s, instrucao[1]) == 1 or recebeRegistro(a, t, s, instrucao[2]) == 1:
            aux = 1
        modificaRegistrador(a, t, s, instrucao[3], aux)        
        pc[0] += 4

    if instrucao[0] == '0110':
        #print(f'{recebeRegistro(a, t, s, instrucao[1])} xor {recebeRegistro(a, t, s, instrucao[2])}?')
        if recebeRegistro(a, t, s, instrucao[1]) != recebeRegistro(a, t, s, instrucao[2]):
            aux = 1
        modificaRegistrador(a, t, s, instrucao[3], aux)        
        pc[0] += 4

    if instrucao[0] == '0111':
        #print(f'{recebeRegistro(a, t, s, instrucao[1])} < {recebeRegistro(a, t, s, instrucao[2])}?')
        if recebeRegistro(a, t, s, instrucao[1]) < recebeRegistro(a, t, s, instrucao[2]):
            aux = 1
        modificaRegistrador(a, t, s, instrucao[3], aux)        
        pc[0] += 4



def separaInstrucao(a, t, s, instrucao, pc, ra):
    if instrucao[0] == '0010' or '0011' or '0100' or '0101' or '0110' or '0111' or '0000' or  '0001':
        executaInstrucaoR(instrucao, a, t, s, pc)

    if instrucao[0] == '1000' or '1001' or '1100' or '1101':
        executaInstrucaoI(instrucao, a, t, s, pc)

    if instrucao[0] == '1010' or '1110' or '1111':
        executaInstrucaoJ(instrucao, a, t, s, pc, ra)


#----------------------------- Funções Print -----------------------------
# Recebe cada instrução presente no vetor de instruções, atráves de busca
# em vetores de tuplas identifica que tipo de instrução é, e armazena o nome
# da instrução na primeira posição de uma lista de vetores; depois disso
# é identificado os registradores e armazenados seus nomes nas respectivas
# posições para impressão. 
def identificaInstrucoes(instrucao, instrucoes_print):
    tipos = [('0010', 'add'), ('0011', 'sub'), ('0100', 'and'), ('0101', 'or'), 
    ('0110', 'xor'), ('0111', 'slt'), ('0000', 'lw'), ('0001', 'sw'), ('1000', 'addi'), 
    ('1001', 'sft'), ('1100', 'beq'), ('1101', 'blt'), ('1010', 'not'), ('1110', 'J'), ('1111', 'Jal')]
    tipo_j_i = ['1000', '1001', '1100', '1101', '1010', '1110', '1111']
    registradores = [('0000', '$zero'), ('0001', '$t0'), ('0010', '$t1'), ('0011', '$t2'),
    ('0100', '$a0'), ('0101', '$a1'), ('0110', '$a2'), ('0111', '$s0'), ('1000', '$s1'),
    ('1001', '$s2'), ('1010', '$s3'), ('1011', '$s4'), ('1100', '$gp'), ('1101', '$sp'),
    ('1110', '$pc'), ('1111', '$ra')]
    #Se quiser adicionar o $zero: ('0000', '$zero'), 

    instrucao_aux = []
    for tipo in tipos:
        if instrucao[0] == tipo[0]:
            instrucao_aux.append(tipo[1])
    for count in range(1, len(instrucao)):
        for reg in registradores:
            if instrucao[count] == reg[0]:
                instrucao_aux.append(reg[1])
                break
    
    # Identifica se o tipo da instrução é do tipo que contém numeros imediatos,
    # se for, ela converte o ultimo itém da instrução em inteiro e armazena
    # na ultima posição do vetor de impressão
    if instrucao[0] in tipo_j_i:
        num = str(int(instrucao[(len(instrucao) - 1)], 2))
        if num != '0':
            instrucao_aux[(len(instrucao_aux) - 1)] = num.strip()
    instrucoes_print.append(instrucao_aux)
        


# Imprime o estado de todos os registradores de maneira formatada
def imprimirRegistradores(a, t, s, ra, pc):
    print(f''' ----------------------------------------------------------------------
 |{"Registradores":^68}|
 ----------------------------------------------------------------------
 | $t0: {t[0]:<7}| $t1: {t[1]:<7}| $t2: {t[2]:<7}|      {"":<7}|      {"":<6}|
 | $a0: {a[0]:<7}| $a1: {a[1]:<7}| $a2: {a[2]:<7}|      {"":<7}|      {"":<6}|
 | $s0: {s[0]:<7}| $s1: {s[1]:<7}| $s2: {s[2]:<7}| $s3: {s[3]:<7}| $s4: {s[4]:<6}|
 | $ra: {ra[0]:<7}| $pc: {pc[0]:<7}|      {"":<7}|      {"":<7}|      {"":<6}|
 ----------------------------------------------------------------------
    ''')



# Identifica quantos itens tem a instrução e de acordo com
# a quantidade ele imprime de maneira formatada
def imprimirInstrucao(instrucao, indice):
    tam = len(instrucao)
    if tam == 4:
        inst = indice + '. ' + instrucao[0] + ' ' + instrucao[1] + ', ' + instrucao[2] + ', ' + instrucao[3]
        print(f' |  {inst:<66}|')
    elif tam == 3:
        inst = indice + '. ' + instrucao[0] + ' ' + instrucao[1] + ', ' + instrucao[2] 
        print(f' |  {inst:<66}|')
    elif tam == 2:
        inst = indice + '. ' + instrucao[0] + ' ' + instrucao[1]
        print(f' |  {inst:<66}|')



# Mesma função de imprimir, porém imprime a instrução que
# está sendo executada na execução passo-a-passo
def imprimirInstrucao_PaP(instrucao, indice):
    tam = len(instrucao)
    if tam == 4:
        inst = indice + '. ' + instrucao[0] + ' ' + instrucao[1] + ', ' + instrucao[2] + ', ' + instrucao[3]
        print(f' |* {inst:<66}|')
    if tam == 3:
        inst = indice + '. ' + instrucao[0] + ' ' + instrucao[1] + ', ' + instrucao[2] 
        print(f' |* {inst:<66}|')
    if tam == 2:
        inst = indice + '. ' + instrucao[0] + ' ' + instrucao[1]
        print(f' |* {inst:<66}|')
        
            

if __name__ == '__main__':
    #arquivoEntrada = open("entradas.txt", "r")
    instrucoes = []
    instrucoes_print = []
    a = [0, 0, 0]
    t = [0, 0, 0]
    s = [0, 0, 0, 0, 0]
    pc = [4]
    ra = [0]
    sp = []

    # Cabeçalho do programa 
    print(f'{"-"*100}\n{"|"}{"SIMULADOR MIPS":^98}|\n{"-"*100}')

    # Entrada do nome do arquivo
    while True:
        try:
            print(f'\n {"Arquivo" :-^58}')
            arquivo = str(input(' Insira o nome do arquivo de entrada: ')) + '.txt'
            arquivoEntrada = open(arquivo, 'r') 
        except FileNotFoundError:
            print(' Erro!! Arquivo de entrada inexistente no diretorio do programa!')
            print(f' {"-" * 58}')
        else:
            print(f' {"-" * 58}')
            break
                
    carregarInstrucoes(arquivoEntrada, instrucoes)
    quantidadeInstrucoes = 4 * len(instrucoes)
    
    # Percorre cada instrução, idetifica cada uma delas e armazena em uma lista de impressão
    for instrucao in instrucoes:
        identificaInstrucoes(instrucao, instrucoes_print)
    
    # Perguntando para o usuario que tipo de execução do código ele quer que aconteça:
    escolha = str(input('\n ---------------Opções de execução do código---------------\n 1. Passo-a-Passo\n 2. Direta\n\n Escolha uma opção de execução: '))
    
    # Verifica se a opção que o usuario informou é válida
    while escolha != '1' and escolha != '2':
        escolha = str(input(' Erro! Opção inválida!!\nDigite novamente: '))   
    print('\n')

    # Execução Passo-a-Passo
    if escolha == '1':
        # Contador que indica o passo que a execução está
        count = 0
        while pc[0] <= quantidadeInstrucoes:
            passo = 'Passo: ' + str(count)
            print(f' {"-"*70}\n |{passo:^68}|\n {"-"*70}')
            print(f' |{"Instruções":^68}|\n {"-"*70}')

            #Indice para auxiliar na numeração das linhas do código
            indice = 1
            for count_aux in range(0, len(instrucoes_print)):
                # Verifica se a instrução a ser impressa é a instrução em execução
                if count_aux == ((pc[0] / 4) - 1):
                    imprimirInstrucao_PaP(instrucoes_print[count_aux], str(indice))
                else:
                    imprimirInstrucao(instrucoes_print[count_aux], str(indice))
                indice += 1
            
            # Imprime o estado dos registradores e avança para a proxima instrução
            imprimirRegistradores(a, t, s, ra, pc) 
            separaInstrucao(a, t, s, instrucoes[int((pc[0] / 4) - 1)], pc, ra)
            count += 1
            input(" Pressione Enter para continuar...")
        exit()
    
    # Execução Direta
    if escolha == '2':
        print(f' {"-"*70}\n |{"Instruções":^68}|\n {"-"*70}')
        
        # Percorre todas a instruções e imprime elas
        for indice, instrucao in enumerate(instrucoes_print):
            imprimirInstrucao(instrucao, str(indice + 1))
        
        # Executa todas as instruções e imprime os registradores
        while pc[0] <= quantidadeInstrucoes:
            separaInstrucao(a, t, s, instrucoes[int((pc[0] / 4) - 1)], pc, ra)    
        imprimirRegistradores(a, t, s, ra, pc)
        exit()
    
    
    arquivoEntrada.close()
