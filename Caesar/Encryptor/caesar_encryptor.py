def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


with open("../../plaintext.txt", "r", encoding="utf-8") as infile:
    plaintext = infile.read()

key = int(input("Enter a key: "))

ciphertext = caesar_encrypt(plaintext, key)

print("\033[92m\nEncrypted ciphertext:")
print(f"\033[97m{ciphertext}")

with open("../Text/caesar_ciphertext.txt", "w", encoding="utf-8") as outfile:
    outfile.write(ciphertext)

print("\033[96m\nCiphertext written to caesar_ciphertext.txt\033[97m")