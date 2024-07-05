import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.backends import default_backend

# Função para gerar e salvar a chave AES
def generate_and_save_aes_key(key_path):
    # Gerar chave AES-128 (16 bytes)
    key = os.urandom(16)

    # Salvar a chave em um arquivo
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

    print(f"Chave AES gerada e salva em: {key_path}")

if __name__ == "__main__":
    key_path = 'key_file.key'
    generate_and_save_aes_key(key_path)
