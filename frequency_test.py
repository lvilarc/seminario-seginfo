import argparse
import os
from scipy.special import erfc
import math

# Função para realizar o teste de frequência
def frequency_test(buf, size):
    alpha = 0.01
    num_0s = 0
    num_1s = 0

    for i in range(size):
        mask = 0x80
        for j in range(8):
            if (buf[i] & mask):
                num_1s += 1
            else:
                num_0s += 1
            mask >>= 1
    
    Sobs = abs(num_0s - num_1s) / math.sqrt(size * 8)
    p_value = erfc(Sobs / math.sqrt(2))

    if p_value < alpha:
        gamma = 0  # baixa entropia
    else:
        gamma = 1  # alta entropia
    
    print(f"p_value: {p_value}")
    return gamma

# Configurando o argparse para aceitar argumentos da linha de comando
parser = argparse.ArgumentParser(description='Perform frequency test on a binary file.')
parser.add_argument('-f', '--file', type=str, required=True, help='The path to the binary file')
args = parser.parse_args()

# Verificar se o arquivo existe
if not os.path.exists(args.file):
    print(f"Erro: Arquivo '{args.file}' não encontrado.")
    exit(1)

# Carregar o arquivo binário
with open(args.file, 'rb') as binary_file:
    binary_data = binary_file.read()
    file_size = len(binary_data)

# Realizar o teste de frequência
entropy_result = frequency_test(binary_data, file_size)

# Determinar o resultado do teste
if entropy_result == 0:
    print(f"O arquivo '{args.file}' possui baixa entropia.")
else:
    print(f"O arquivo '{args.file}' possui alta entropia.")
