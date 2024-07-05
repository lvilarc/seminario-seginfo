import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Função para criptografar dados usando AES-128 no modo ECB
def encrypt_aes_ecb(key, data):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = data + b'\0' * (16 - len(data) % 16)  # Padding para garantir múltiplos de 16 bytes
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_data

# Configurando o argparse para aceitar argumentos da linha de comando
parser = argparse.ArgumentParser(description='Encrypt a file using AES-128 in ECB mode.')
parser.add_argument('-f', '--file', type=str, required=True, help='The path to the file to be encrypted')
parser.add_argument('-k', '--key', type=str, required=True, help='The path to the AES key file')
args = parser.parse_args()

# Verificar se o arquivo de chave existe
if not os.path.exists(args.key):
    print(f"Erro: Arquivo de chave '{args.key}' não encontrado.")
    exit(1)

# Carregar a chave do arquivo
with open(args.key, 'rb') as key_file:
    key = key_file.read()

# Caminho para o arquivo a ser criptografado
file_path = args.file

# Leitura do arquivo
with open(file_path, 'rb') as file:
    original_data = file.read()

# Criptografar o arquivo usando AES-128 no modo ECB
encrypted_data = encrypt_aes_ecb(key, original_data)

# Salvar o texto cifrado em um novo arquivo
encrypted_file_path = "e_" + file_path
with open(encrypted_file_path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

print(f"Arquivo criptografado com sucesso. Arquivo criptografado salvo em: {encrypted_file_path}")
