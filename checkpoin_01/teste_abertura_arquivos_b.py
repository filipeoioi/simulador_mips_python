#-Objetivo: Abrir arquivos binários e lê-los

#Necessario utilizar a biblioteca pickle
import pickle

'''
Para escrever um objeto em um arquivo utiliza-se o método
pickle.dump, e para lê um objeto utiliza-se o método pickle.load
'''
try:
    arquivo = open('ex03.txt', 'r')
    texto = arquivo.read()
    arquivo.close()
except:
    print('Erro ao ler o arquivo texto')

try: 
    arquivo = open('teste.b', 'wb')
    pickle.dump(texto, arquivo)
    arquivo.close()
except:
    print('Erro ao escrever no arquivo binario!!')

try:
    arquivo = open('teste.b', 'rb')
    conteudo = pickle.load(arquivo)
    print(conteudo)
    arquivo.close()
except:
    print('Erro na leitura do arquivo!!')