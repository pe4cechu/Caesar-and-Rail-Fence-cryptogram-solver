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


with open("plaintext.txt", "r", encoding="utf-8") as infile:
    plaintext = infile.read()

key = int(input("Enter a key: "))

with open("rail_fence_ciphertext.txt", "w", encoding="utf-8") as outfile:
    outfile.write(rail_fence_encrypt(plaintext, key))

print("Ciphertext written to rail_fence_ciphertext.txt")