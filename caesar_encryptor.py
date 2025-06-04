def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


with open("plaintext.txt", "r", encoding="utf-8") as infile:
    plaintext = infile.read()

key = int(input("Enter a key: "))

with open("caesar_ciphertext.txt", "w", encoding="utf-8") as outfile:
    outfile.write(caesar_encrypt(plaintext, key))

print("Ciphertext written to caesar_ciphertext.txt")