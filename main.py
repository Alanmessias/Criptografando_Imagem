from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import io

# Função para Gerar uma Chave AES

def generate_key():
    key = get_random_bytes(16)
    with open("aes_key.key","wb") as key_file:
        key_file.write(key)

# Função para carregar a chave
def load_key():
    return open("aes_key.key","rb").read()

# Criptografando a imagem
def encrypt_image(image_path,output_path):
    key = load_key()
    cipher = AES.new(key,AES.MODE_CBC)
    iv = cipher.iv

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    encrypted_data = iv + cipher.encrypt(pad(image_data,AES.block_size))

    with open(output_path,"wb") as encrypted_file:

        encrypted_file.write(encrypted_data)


# Descriptografando a Imagem
def decrypt_image(encrypted_path, output_path):
    key = load_key()

    with open(encrypted_path,"rb") as enccrypted_file:
        enccrypted_data = enccrypted_file.read()

    iv = enccrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)

    decrpt_data = unpad(cipher.decrypt(enccrypted_data[16:]),AES.block_size)

    with open(output_path, "wb") as image_file:
        image_file.write(decrpt_data)

    if __name__ == "__main__":
        generate_key() # Gera a chave apenas uma vez

    #Caminho dos arquivos
    image_path = "sua_imagem.jpg.jpg"

    encrypted_path = "imagem_criptografada.enc"

    decrypt_path = "imagem_descripgrafada.jpg"

    # Criptografar e descriptografar a imagem

    encrypt_image(image_path, encrypted_path)

    decrypt_image(encrypted_path,decrypt_path)

print("Imagem criptografada e descriptografada com sucesso")

