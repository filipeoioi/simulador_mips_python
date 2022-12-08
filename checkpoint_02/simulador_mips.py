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

        print(f'inverteu o valor do registrador {instrucao[1]}')

        pc[0] += 4

    if instrucao[0] == '1110':
        ins = instrucao[2] + instrucao[3]
        print(f"Jumpando para {int(ins, 2) * 4}")
        pc[0] = int(ins, 2) * 4

    if instrucao[0] == '1111':
        ins = instrucao[2] + instrucao[3]
        print(f"Jumpando para {int(ins, 2) * 4}")
        ra[0] = pc[0]
        pc[0] = int(ins, 2) * 4
        return
          
def executaInstrucaoI(instrucao, a, t, s, pc):
    if instrucao[0] == '1000':
        numeroDecimal = int(instrucao[3], 2)
        somaRegistrador(a, t, s, instrucao[2], numeroDecimal)
        print(f'somando {numeroDecimal} em {instrucao[2]}')
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

        print(f'shiftando o registro {binario} para {"".join(binarios)} e salvando em {instrucao[2]} ')
        pc[0] += 4

    if instrucao[0] == '1100':
        if recebeRegistro(a, t, s, instrucao[1]) == recebeRegistro(a, t, s, instrucao[2]):
            pc[0] = int(instrucao[3], 2) * 4
            print("Comparacao sucesso")
            return
        print("Comparacao falhou")
        pc[0] += 4

    if instrucao[0] == '1101':
        if recebeRegistro(a, t, s, instrucao[1]) < recebeRegistro(a, t, s, instrucao[2]):
            pc[0] = int(instrucao[3], 2) * 4
            print("Comparacao sucesso")
            return
        print("Comparacao falhou")
        pc[0] += 4
def executaInstrucaoR(instrucao, a, t, s, pc):
    aux = 0

    if instrucao[0] == '0010':
        print(f'{recebeRegistro(a, t, s, instrucao[1])} + {recebeRegistro(a, t, s, instrucao[2])}')
        modificaRegistrador(a, t, s, instrucao[3], (recebeRegistro(a, t, s, instrucao[1]) + recebeRegistro(a, t, s, instrucao[2])))    
        pc[0] += 4
    
    if instrucao[0] == '0011':
        print(f'{recebeRegistro(a, t, s, instrucao[1])} - {recebeRegistro(a, t, s, instrucao[2])}')
        modificaRegistrador(a, t, s, instrucao[3], (recebeRegistro(a, t, s, instrucao[1]) - recebeRegistro(a, t, s, instrucao[2])))        
        pc[0] += 4

    if instrucao[0] == '0100':
        print(f'{recebeRegistro(a, t, s, instrucao[1])} and {recebeRegistro(a, t, s, instrucao[2])} = 1?')
        if recebeRegistro(a, t, s, instrucao[1]) == recebeRegistro(a, t, s, instrucao[2]) == 1:
            aux = 1
        modificaRegistrador(a, t, s, instrucao[3], aux)        
        pc[0] += 4

    if instrucao[0] == '0101':
        print(f'{recebeRegistro(a, t, s, instrucao[1])} or {recebeRegistro(a, t, s, instrucao[2])} = 1?')
        if recebeRegistro(a, t, s, instrucao[1]) == 1 or recebeRegistro(a, t, s, instrucao[2]) == 1:
            aux = 1
        modificaRegistrador(a, t, s, instrucao[3], aux)        
        pc[0] += 4

    if instrucao[0] == '0110':
        print(f'{recebeRegistro(a, t, s, instrucao[1])} xor {recebeRegistro(a, t, s, instrucao[2])}?')
        if recebeRegistro(a, t, s, instrucao[1]) != recebeRegistro(a, t, s, instrucao[2]):
            aux = 1
        modificaRegistrador(a, t, s, instrucao[3], aux)        
        pc[0] += 4

    if instrucao[0] == '0111':
        print(f'{recebeRegistro(a, t, s, instrucao[1])} < {recebeRegistro(a, t, s, instrucao[2])}?')
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

def imprimirRegistradores(a, t, s, ra):
    arquivoSaida = open("saida.txt", "w")
    arquivoSaida.write(f't0: {t[0]}\nt1: {t[1]}\nt2: {t[2]}\na0: {a[0]}\na1: {a[1]}\na2: {a[2]}\ns0: {s[0]}\ns1: {s[1]}\ns2: {s[2]}\ns3: {s[3]}\ns4: {s[4]}\n\nra: {ra[0]}')
    arquivoSaida.close()

def main():
    arquivoEntrada = open("entradas.txt", "r")
    instrucoes = []
    a = [0, 0, 0]
    t = [0, 0, 0]
    s = [0, 0, 0, 0, 0]
    pc = [4]
    ra = [0]
    sp = []

    carregarInstrucoes(arquivoEntrada, instrucoes)
    quantidadeInstrucoes = 4 * len(instrucoes)

    #print("inicial:")
    #print(a, t, s)

    while(pc[0] <= quantidadeInstrucoes):
        print(f'Pc: {pc[0]}', end=' ')
        separaInstrucao(a, t, s, instrucoes[int((pc[0] / 4) - 1)], pc, ra)

    imprimirRegistradores(a, t, s, ra)
    arquivoEntrada.close()

main()