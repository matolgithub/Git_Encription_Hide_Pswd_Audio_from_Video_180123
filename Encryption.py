import pyAesCrypt
from os import walk


def encrypt_file():
    encrypt_files_name = []
    encrypt_file_path = "encrypt/"
    for (dirpath, dirnames, filenames) in walk(encrypt_file_path):
        encrypt_files_name.extend(filenames)
        break
    # print(encrypt_files_name)
    for file in encrypt_files_name:
        password = input("Please, input your password for encrypting the file: ")
        new_file_name = f"{file}.aes"

        # encrypt
        pyAesCrypt.encryptFile(f"{encrypt_file_path}{file}", f"{encrypt_file_path}{new_file_name}", password)

        # decrypt
        pyAesCrypt.decryptFile(f"{encrypt_file_path}{new_file_name}",
                               f"{encrypt_file_path}decrypt_{new_file_name[:-4]}", password)


if __name__ == "__main__":
    encrypt_file()
