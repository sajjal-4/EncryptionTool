import string
from math import gcd

def additive_cipher(plaintext,key):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char) - 65 + key) % 26 + 65 if char.isupper() else (ord(char) - 97 + key) % 26 + 97
            encrypted += chr(shift)
        else:
            encrypted += char
    return encrypted

def multiplicative_cipher(plaintext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26.")
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char) - 65) * key % 26 + 65 if char.isupper() else (ord(char) - 97) * key % 26 + 97
            encrypted += chr(shift)
        else:
            encrypted += char
    return encrypted

def affine_cipher(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift = (a * (ord(char) - 65) + b) % 26 + 65 if char.isupper() else (a * (ord(char) - 97) + b) % 26 + 97
            encrypted += chr(shift)
        else:
            encrypted += char
    return encrypted

def monoalphabetic_substitution(plaintext, substitution_key):
    alphabet = string.ascii_lowercase
    encrypted = ""
    for char in plaintext:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_char = substitution_key[index].upper() if char.isupper() else substitution_key[index]
            encrypted += new_char
        else:
            encrypted += char
    return encrypted

def autokey_cipher(plaintext, keyword):
    keyword = keyword.lower()
    extended_key = keyword + plaintext
    encrypted = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = extended_key[i].lower()
            shift = (ord(char) - 97 + ord(key_char) - 97) % 26 + 97
            encrypted += chr(shift)
        else:
            encrypted += char
    return encrypted

def playfair_cipher(plaintext, keyword):
    # Placeholder for Playfair cipher implementation
    return "Playfair cipher not implemented."

def vigenere_cipher(plaintext, keyword):
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    encrypted = ""
    for p, k in zip(plaintext, keyword):
        if p.isalpha():
            shift = (ord(p.lower()) - 97 + ord(k.lower()) - 97) % 26 + 97
            encrypted += chr(shift).upper() if p.isupper() else chr(shift)
        else:
            encrypted += p
    return encrypted

def keyless_transposition(plaintext):
    # Placeholder for Keyless Transposition implementation
    return "Keyless Transposition not implemented."

def keyed_transposition(plaintext, key):
    # Placeholder for Keyed Transposition implementation
    return "Keyed Transposition not implemented."

def combination_cipher(plaintext, key):
    # Placeholder for Combination of Keyless and Keyed approaches
    return "Combination cipher not implemented."

def double_transposition(plaintext, key1, key2):
    # Placeholder for Double Transposition implementation
    return "Double Transposition not implemented."

# User Interface

def display_menu():
    print("\n" + "="*40)
    print(" 🛡️ Welcome to the Encryption Tool! ")
    print("="*40)
    print("Select a cipher:")
    print("1. Additive Cipher")
    print("2. Multiplicative Cipher")
    print("3. Affine Cipher")
    print("4. Monoalphabetic Substitution Cipher")
    print("5. Autokey Cipher")
    print("6. Playfair Cipher")
    print("7. Vigenère Cipher")
    print("8. Keyless Transposition")
    print("9. Keyed Transposition")
    print("10. Combination of Keyless and Keyed Approaches")
    print("11. Double Transposition Cipher")
    print("0. Exit")
    print("="*40)

def get_valid_choice():
    while True:
        choice = input("Enter your choice (0-11): ")
        if choice.isdigit() and 0 <= int(choice) <= 11:
            return int(choice)
        else:
            print("Invalid input. Please enter a digit between 0 and 11.")

def main():
    while True:
        display_menu()
        choice = get_valid_choice()

        if choice == 0:
            print("Exiting the tool. Goodbye! 👋")
            break

        plaintext = input("Enter the plaintext: ").strip()

        if choice == 1:
            key = int(input("Enter the key (integer): "))
            result = additive_cipher(plaintext, key)
        elif choice == 2:
            key = int(input("Enter the key (must be coprime with 26): "))
            result = multiplicative_cipher(plaintext, key)
        elif choice == 3:
            a = int(input("Enter key 'a' (must be coprime with 26): "))
            b = int(input("Enter key 'b': "))
            result = affine_cipher(plaintext, a, b)
        elif choice == 4:
            substitution_key = input("Enter the substitution key (26 letters): ")
            result = monoalphabetic_substitution(plaintext, substitution_key)
        elif choice == 5:
            keyword = input("Enter the keyword: ")
            result = autokey_cipher(plaintext, keyword)
        elif choice == 6:
            keyword = input("Enter the keyword: ")
            result = playfair_cipher(plaintext, keyword)
        elif choice == 7:
            keyword = input("Enter the keyword: ")
            result = vigenere_cipher(plaintext, keyword)
        elif choice == 8:
            result = keyless_transposition(plaintext)
        elif choice == 9:
            key = input("Enter the key: ")
            result = keyed_transposition(plaintext, key)
        elif choice == 10:
            key = input("Enter the key: ")
            result = combination_cipher(plaintext, key)
        elif choice == 11:
            key1 = input("Enter the first key: ")
            key2 = input("Enter the second key: ")
            result = double_transposition(plaintext, key1, key2)

        print("\n" + "="*40)
        print("🔐 Result:")
        print("Ciphertext: ", result)
        print("="*40)

if __name__ == "__main__":
    main()
