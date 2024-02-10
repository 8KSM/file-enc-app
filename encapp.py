import os
from cryptography.fernet import Fernet

file_path = input("파일의 경로를 입력하세요 :")
case = int(input("encrypted(1) derypted(2) :"))

filename = file_path
enc_filename = filename + ".enc"

if(case == 1):
    key = Fernet.generate_key()
    print(key)
    cipher = Fernet(key)
    with open(file_path, "rb") as file_in:
        encrypted_data = cipher.encrypt(file_in.read())
    with open(enc_filename, "wb") as file_out:
        file_out.write(encrypted_data)
    os.remove(file_path)
    print("encrypted.")

elif(case == 2):
    dec_key = input("복호화 key를 입력하세요 :")
    cipher = Fernet(dec_key)
    with open(file_path, "rb") as file_in:
        decrypted_data = cipher.decrypt(file_in.read())
    with open(file_path, "wb") as file_out:
        file_out.write(decrypted_data)
    print("decrypted.")
    if filename.endswith(".enc"):
        original_filename = filename[:-4]
        os.rename(filename, original_filename)
else :
    exit()
