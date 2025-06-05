def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted = chr((ord(char) - base - shift) % 26 + base)
            plaintext += decrypted
        else:
            plaintext += char
    return plaintext

with open("../Text/caesar_ciphertext.txt", "r", encoding="utf-8") as infile:
    ciphertext = infile.read()

key = int(input("Enter the decryption key (shift): "))

plaintext = caesar_decrypt(ciphertext, key)

print("\033[92m\nDecrypted plaintext:")
print(f"\033[97m{plaintext}")

with open("../Text/caesar_plaintext.txt", "w", encoding="utf-8") as outfile:
    outfile.write(plaintext)

print("\033[96m\nPlaintext written to caesar_plaintext.txt\033[97m")