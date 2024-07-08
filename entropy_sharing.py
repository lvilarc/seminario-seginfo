import os
import argparse
import time

def generate_shares(encrypted_file_path, benign_file_path, m):
    # Ler os arquivos
    with open(encrypted_file_path, 'rb') as ef, open(benign_file_path, 'rb') as bf:
        encrypted_data = ef.read()
        benign_data = bf.read()
    
    # Verificar se o arquivo benigno tem tamanho suficiente
    if len(benign_data) < len(encrypted_data) * m:
        raise ValueError("O arquivo benigno é muito pequeno para o valor de m especificado.")

    start_time = time.time()
    shares = []

    # Gerar shares
    for i in range(len(encrypted_data)):
        subbyte = encrypted_data[i]
        benign_bytes = benign_data[i * m : (i + 1) * m]
        share = bytearray(benign_bytes)
        
        # Calcular o ai
        ai = subbyte
        for j in range(m):
            ai ^= share[j]
        
        shares.append((share, ai))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")
    return shares

def save_modified_file(shares, output_file_path):
    with open(output_file_path, 'wb') as mf:
        for share, ai in shares:
            mf.write(share)
            mf.write(bytes([ai]))

def main():
    parser = argparse.ArgumentParser(description="Script para gerar shares e salvar o arquivo modificado.")
    parser.add_argument('-f', '--file', required=True, help='Caminho para o arquivo criptografado.')
    parser.add_argument('-bf', '--benign', required=True, help='Caminho para o arquivo benigno.')
    parser.add_argument('-m', '--shares', type=int, required=True, help='Número de shares por byte.')

    args = parser.parse_args()

    encrypted_file_path = args.file
    benign_file_path = args.benign
    m = args.shares

    shares = generate_shares(encrypted_file_path, benign_file_path, m)
    
    output_file_path = os.path.join(os.path.dirname(encrypted_file_path), 'shared_' + os.path.basename(encrypted_file_path))
    save_modified_file(shares, output_file_path)

    print(f"Arquivo modificado salvo em: {output_file_path}")

if __name__ == '__main__':
    main()
