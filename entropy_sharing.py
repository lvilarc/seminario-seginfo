import argparse
import os

def entropy_sharing(input_file, benign_file, m):
    with open(benign_file, 'rb') as bf:
        benign_data = bf.read()

    with open(input_file, 'rb') as f:
        input_data = f.read()

    n = len(input_data)  # número de bytes no arquivo de entrada

    output_data = bytearray()

    # Processar cada byte do arquivo de entrada
    for byte in input_data:
        shares = bytearray()
        # Gerar m shares para cada byte
        for i in range(m):
            # Exemplo de operação de entropy sharing simples
            share = (byte ^ benign_data[i % len(benign_data)]) & 0xFF  # XOR com byte do benign_file
            shares.append(share)
        # Adicionar o byte original e os shares ao output_data
        output_data.append(byte)
        output_data.extend(shares)

    # Obter a extensão do arquivo de entrada
    file_ext = os.path.splitext(input_file)[1]
    # Criar o nome do arquivo de saída com a mesma extensão
    output_file = input_file.replace(file_ext, f'_shared{file_ext}')

    # Escrever o resultado no novo arquivo
    with open(output_file, 'wb') as out:
        out.write(output_data)

    print(f"Entropy sharing concluído. Resultados salvos em '{output_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform entropy sharing on a file.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Input file for entropy sharing')
    parser.add_argument('-bf', '--benign-file', type=str, required=True, help='Benign file for entropy sharing')
    parser.add_argument('-m', '--shares', type=int, default=4, help='Number of shares to generate per byte (default: 4)')
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Erro: Arquivo '{args.file}' não encontrado.")
        exit(1)
    
    if not os.path.exists(args.benign_file):
        print(f"Erro: Arquivo benigno '{args.benign_file}' não encontrado.")
        exit(1)

    entropy_sharing(args.file, args.benign_file, args.shares)
