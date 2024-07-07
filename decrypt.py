import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import time

# Função para decifrar dados usando AES-128 no modo ECB
def decrypt_aes_ecb(key, encrypted_data):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remover o padding PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return decrypted_data

# Configurando o argparse para aceitar argumentos da linha de comando
parser = argparse.ArgumentParser(description='Decrypt a file encrypted with AES-128 in ECB mode.')
parser.add_argument('-f', '--file', type=str, required=True, help='The path to the encrypted file')
parser.add_argument('-k', '--key', type=str, required=True, help='The path to the AES key file')
args = parser.parse_args()

# Verificar se o arquivo de chave existe
if not os.path.exists(args.key):
    print(f"Erro: Arquivo de chave '{args.key}' não encontrado.")
    exit(1)

# Carregar a chave do arquivo
with open(args.key, 'rb') as key_file:
    key = key_file.read()

# Caminho para o arquivo cifrado
encrypted_file_path = args.file

# Leitura do arquivo cifrado
with open(encrypted_file_path, 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

start_time = time.time()
# Decifrar o arquivo usando AES-128 no modo ECB
decrypted_data = decrypt_aes_ecb(key, encrypted_data)
end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")

# Determinar o caminho para salvar o arquivo decifrado
decrypted_file_path = "d_" + os.path.basename(encrypted_file_path)

# Salvar os dados decifrados em um novo arquivo
with open(decrypted_file_path, 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)

print(f"Arquivo decifrado com sucesso. Arquivo decifrado salvo em: {decrypted_file_path}")
