def rail_fence_decrypt(ciphertext, num_rails):
    if num_rails <= 1 or num_rails >= len(ciphertext):
        return ciphertext

    pattern = [0] * len(ciphertext)
    rail = 0
    direction = 1

    for i in range(len(ciphertext)):
        pattern[i] = rail
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction

    rails = [[] for _ in range(num_rails)]
    rail_counts = [pattern.count(r) for r in range(num_rails)]

    idx = 0
    for r in range(num_rails):
        rails[r] = list(ciphertext[idx:idx+rail_counts[r]])
        idx += rail_counts[r]

    result = []
    rail_indices = [0] * num_rails
    for r in pattern:
        result.append(rails[r][rail_indices[r]])
        rail_indices[r] += 1

    return ''.join(result)


with open("../Encryptor/rail_fence_ciphertext.txt", "r", encoding="utf-8") as infile:
    ciphertext = infile.read()

key = int(input("Enter a key: "))

decrypted = rail_fence_decrypt(ciphertext, key)

# Print plaintext to the console
print("\nDecrypted plaintext:\n")
print(decrypted)

with open("rail_fence_plaintext.txt", "w", encoding="utf-8") as outfile:
    outfile.write(decrypted)

print("\nPlaintext written to rail_fence_plaintext.txt")