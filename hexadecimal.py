import argparse
import os

# Configurando o argparse para aceitar argumentos da linha de comando
parser = argparse.ArgumentParser(description='Exibe a chave AES em formato hexadecimal.')
parser.add_argument('-k', '--key', type=str, required=True, help='O caminho para o arquivo da chave AES')
args = parser.parse_args()

# Verificar se o arquivo de chave existe
if not os.path.exists(args.key):
    print(f"Erro: Arquivo de chave '{args.key}' não encontrado.")
    exit(1)

# Carregar a chave do arquivo
with open(args.key, 'rb') as key_file:
    key = key_file.read()

# Converter para representação hexadecimal
hex_key = "0x" + key.hex().upper()

# Imprimir a chave em formato hexadecimal
print("Chave AES em formato hexadecimal:", hex_key)
