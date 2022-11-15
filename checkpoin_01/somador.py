def somador_basico(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    res = []
    sobra = '0'
    for count in range(0, 4):
        if num1[count] == '1' and num2[count] == '1' and sobra == '0':
            res.append('0')
            sobra = '1'
        elif num1[count] == '1' and num2[count] == '0' and sobra == '0':
            res.append('1')
            sobra = '0'
        elif num1[count] == '0' and num2[count] == '1' and sobra == '0':
            res.append('1')
            sobra = '0'
        elif num1[count] == '1' and num2[count] == '1' and sobra == '1':
            res.append('1')
            sobra = '1'
        elif num1[count] == '1' and num2[count] == '0' and sobra == '1':
            res.append('0')
            sobra = '1'
        elif num1[count] == '0' and num2[count] == '1' and sobra == '1':
            res.append('0')
            sobra = '1'
        elif num1[count] == '0' and num2[count] == '0' and sobra == '0':
            res.append('0')
            sobra = '0'
        elif num1[count] == '0' and num2[count] == '0' and sobra == '1':
            res.append('1')
            sobra = '0'
        print(res)
    res = ''.join(res)
    res = res[::-1]
    return res

num1 = '0001'
num2 = '0010'
#Resultado = '0100'
res = somador_basico(num1, num2)
print(res)