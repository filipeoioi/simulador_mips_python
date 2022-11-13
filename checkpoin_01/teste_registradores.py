lista_regs = []
regs = {'simbolo' : '$t1', 'cod' : '0010', 'conteudo' : '0000', 'op' : '0010'}
lista_regs.append(regs)
regs = {'simbolo' : '$t0', 'cod' : '0001', 'conteudo' : '0000'}
lista_regs.append(regs)

codigo_texto = '0001 0111'
conteudo_texto = codigo_texto.split()
cod = conteudo_texto[0]
numero = conteudo_texto[1]

for count in range(0, len(lista_regs)):
    if cod == lista_regs[count]['cod']:
        reg = lista_regs[count]['simbolo']
        lista_regs[count]['conteudo'] = numero
        conteudo = lista_regs[count]['conteudo']
        print(f'O registrador é {reg}')
        print(f'O conteudo desse registrador é {conteudo}')
    
print(len(lista_regs[1]))


