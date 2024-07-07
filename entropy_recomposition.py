import os
import argparse

def reconstruct_data(modified_file_path, m):
    with open(modified_file_path, 'rb') as mf:
        modified_data = mf.read()

    shares = []
    data_length = len(modified_data) // (m + 1)
    
    for i in range(data_length):
        start = i * (m + 1)
        share = modified_data[start:start + m]
        ai = modified_data[start + m]
        shares.append((share, ai))
    
    reconstructed_data = bytearray()

    for share, ai in shares:
        subbyte = ai
        for j in range(m):
            subbyte ^= share[j]
        reconstructed_data.append(subbyte)

    return reconstructed_data

def main():
    parser = argparse.ArgumentParser(description="Script para reconstruir dados a partir do arquivo modificado.")
    parser.add_argument('-sf', '--sharedFile', required=True, help='Caminho para o arquivo modificado.')
    parser.add_argument('-m', '--shares', type=int, required=True, help='Número de shares por byte.')

    args = parser.parse_args()

    modified_file_path = args.sharedFile
    m = args.shares

    reconstructed_data = reconstruct_data(modified_file_path, m)
    
    output_file_path = os.path.join(os.path.dirname(modified_file_path), 'reconstructed_' + os.path.basename(modified_file_path))
    with open(output_file_path, 'wb') as rf:
        rf.write(reconstructed_data)

    print(f"Dados reconstruídos salvos em: {output_file_path}")

if __name__ == '__main__':
    main()
