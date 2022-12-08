tipo_r = [('0010', 'add'), ('0011', 'sub'), ('0100', 'and'), ('0101', 'or'), ('0110', 'xor'), ('0111', 'slt'), ('0000', 'lw'), ('0001', 'sw')]
ins = '0100'
for inst in tipo_r:
    if ins == inst[0]:
        print(inst[1])
if ins in tipo_r:
    print('ESTÁ DENTRO')

num_b = '0011'
num = int(num_b, 2)
print(num)