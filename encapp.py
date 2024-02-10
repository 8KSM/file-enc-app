import os
from cryptography.fernet import Fernet

directory = input("파일의 경로를 입력하세요 :")
case = int(input("encrypted(1) derypted(2) :"))

filename = directory

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_dir(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files :
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path)

def decrypt_dir(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files :
            file_path = os.path.join(root, file_name)
            if file_path.endswith(".enc"):
                decrypt_file(file_path)

def encrypt_file(file_path):
    with open(file_path, "rb") as file_in:
        encrypted_data = cipher.encrypt(file_in.read())
    enc_filename = file_path + ".enc"
    with open(enc_filename, "wb") as file_out:
        file_out.write(encrypted_data)
    os.remove(file_path)
    print(f"Encrypted {file_path}.")

def decrypt_file(file_path):
    if not file_path.endswith(".enc"):
        return
    cipher = Fernet(dec_key)
    with open(file_path, "rb") as file_in:
        decrypted_data = cipher.decrypt(file_in.read())
    with open(file_path, "wb") as file_out:
        file_out.write(decrypted_data)
    print(f"Decrypted {file_path}.")
    if file_path.endswith(".enc"):
        original_filename = file_path[:-4]
        os.rename(file_path, original_filename)

if(case == 1):
    print("Generated key:", key)
    encrypt_dir(directory)

elif(case == 2):
    dec_key = input("복호화 key를 입력하세요 :")
    decrypt_dir(directory)

else:
    exit()