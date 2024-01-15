import getpass
import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


salt = b'18d062109d9aa4dc5797e5521888e3e6' # chaine de caracteres de aléatoire de 16 bits


def hash_password(password):
    hashed_password = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)

    if len(hashed_password) > 32:
        hashed_password = hashed_password[:32]

    return hashed_password


def hash_password_aes(password):

    # Utiliser SHA-256 pour le hachage, produisant un hachage de 32 octets
    sha256_hash = hashlib.sha256(b'password_bytes' + b'salt_bytes').digest()

    return sha256_hash



def sign_up():
    login = input("Entrez le nom d'utilisateur: ")
    password = getpass.getpass("Entrez le mot de passe: ")

    hashed_password = hash_password(password)

    with open("user_data.txt", "a") as file:
        file.write(f"{login}:{hashed_password.hex()}\n")
    print("Enregistrement réussi ")


def sign_in():
    login = input("Entrez le nom de l'utilisateur: ")
    password = getpass.getpass("Entrez le mot de passe: ")

    with open("user_data.txt", "r") as file:
        for line in file:
            stored_login, stored_hashed_password = line.strip().split(":")            
            if login == stored_login:
                hashed_password = hash_password(password)
                if hashed_password.hex() == stored_hashed_password:
                    print("Vérification réussie")
                    return 0

    print("Login ou mot de passe incorrects. Réessayez.")
    return 1


def encode_file(filename, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(filename, 'rb') as file:
        plaintext = file.read()
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(f"{filename}.enc", 'wb') as file:
        file.write(cipher.iv + ciphertext)
    print(f"Chiffrement du fichier réussi. Fichier chiffré: {filename}.enc")


def encrypt_existing_file():
    login = input("Entrez le nom de l'utilisateur: ")
    password = getpass.getpass("Entrez le mot de passe: ")

    with open("user_data.txt", "r") as file:
        for line in file:
            stored_login, stored_hashed_password = line.strip().split(":")            
            if login == stored_login:
                hashed_password = hash_password(password)

                if hashed_password.hex() == stored_hashed_password:
                    print("Vérification réussie")
                    filename = input("Entrez le nom du fichier à chiffrer: ")
                    # on ne veut surtout pas avoir le même mot de passe que celui dans le fichier de données d'utilisateur



                    encode_file(filename, hash_password_aes(password))
                    break
            else:
                print("L'utilisateur n'existe pas")


def decode_file(filename, key):
    try:
        with open(f"{filename}", 'rb') as file:
            # Read the IV (initialization vector)
            iv = file.read(16)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            
            # Decrypt the file
            ciphertext = file.read()
            decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)

        with open(f"{filename}_decoded.txt", 'wb') as file:
            file.write(decrypted_text)

        print(f"Déchiffrement du fichier réussi. Fichier déchiffré: {filename}_decoded.txt")

    except Exception as e:
        print(f"Erreur lors du déchiffrement du fichier : {e}")



def decrypt_existing_file():
    login = input("Entrez le nom de l'utilisateur: ")
    password = getpass.getpass("Entrez le mot de passe: ")

    with open("user_data.txt", "r") as file:
        for line in file:
            stored_login, stored_hashed_password = line.strip().split(":")
            if login == stored_login:
                hashed_password = hash_password(password)

                if hashed_password.hex() == stored_hashed_password:
                    print("Vérification réussie")
                    filename = input("Entrez le nom du fichier à déchiffrer: ")
                    decode_file(filename, hash_password_aes(password))
                    break
        else:
            print("L'utilisateur n'existe pas")


def main():
    while True:
        print("\n1. S'inscrire\n2. Vérifier les identifiants\n3. Chiffrer un fichier\n4. Déchiffrer un fichier\n5. Quitter")
        choice = input("Entrez votre choix (1/2/3/4/5): ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            encrypt_existing_file()
        elif choice == "4":
            decrypt_existing_file()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Choix invalide, veuillez entrer 1, 2, 3, 4, ou 5")


if __name__ == "__main__":
    main()
