def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def rail_fence_encrypt(text, num_rails):
    if num_rails <= 1 or num_rails >= len(text):
        return text
    rails = ['' for _ in range(num_rails)]
    rail = 0
    direction = 1
    for char in text:
        rails[rail] += char
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction
    return ''.join(rails)

def hybrid_encrypt(text, hybrid_key):
    caesar_text = caesar_encrypt(text, hybrid_key)
    rail_text = rail_fence_encrypt(caesar_text, hybrid_key)
    return rail_text
git push origin main

with open("plaintext.txt", "r", encoding="utf-8") as infile:
    plaintext = infile.read()

# key = int(input("Enter a key: "))
key = 3
ciphertext = hybrid_encrypt(plaintext, key)

with open("hybrid_ciphertext.txt", "w", encoding="utf-8") as outfile:
    outfile.write(ciphertext)

print("Hybrid encryption complete! See hybrid_ciphertext.txt for the result.")