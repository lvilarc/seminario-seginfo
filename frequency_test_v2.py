import argparse
import os
from scipy.special import erfc
import math

# Teste de frequência
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
    
    return p_value, gamma

parser = argparse.ArgumentParser(description='Perform frequency test on a binary file.')
parser.add_argument('-f', '--file', type=str, required=True, help='The path to the binary file')
args = parser.parse_args()

if not os.path.exists(args.file):
    print(f"Erro: Arquivo '{args.file}' não encontrado.")
    exit(1)

with open(args.file, 'rb') as binary_file:
    binary_data = binary_file.read()
    file_size = len(binary_data)

# Dividir o arquivo em 100 sequências binárias
segment_size = file_size // 100
remainder = file_size % 100

p_values = []

start_index = 0
for i in range(100):
    end_index = start_index + segment_size + (1 if i < remainder else 0)  # Ajusta para distribuir o resto
    segment = binary_data[start_index:end_index]
    
    p_value, entropy_result = frequency_test(segment, len(segment))
    p_values.append(p_value)
    
    start_index = end_index

# Calcular a taxa de sucesso (pass rate)
pass_rate = sum(1 for p_value in p_values if p_value >= 0.01) / 100
average_p_value = sum(p_values) / 100

# Exibir resultados
print(f"Pass rate: {pass_rate}")
print(f"Average p-value: {average_p_value:.6f}")

# Determinar o resultado do teste
if pass_rate >= 0.96:
    print(f"O arquivo '{args.file}' pode ser classificado como aleatório.")
else:
    print(f"O arquivo '{args.file}' não pode ser classificado como aleatório.")
