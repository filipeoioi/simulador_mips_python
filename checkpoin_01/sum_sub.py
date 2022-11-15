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
    res = ''.join(res)
    res = res[::-1]
    return res

def complemento_2(num):
    res = []
    numero1 = '0001'
    for count in range(0, len(num)):
        if num[count] == '1':
            res.append('0') 
        elif num[count] == '0':
            res.append('1')
    res = ''.join(res)
    res = somador_basico(res, numero1)
    num = res
    return num

def sub(num1, num2):
    num2 = complemento_2(num2)
    res = somador_basico(num1, num2)
    return res


