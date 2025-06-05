from math import sqrt
from nostril import nonsense

with open("../Text/caesar_ciphertext.txt", "r", encoding="utf-8") as infile:
    ciphertext = infile.read()

plaintext = ""
plain = []
occ_dict = {
    "E": 12.31,
    "T": 9.59,
    "A": 8.05,
    "O": 7.94,
    "N": 7.19,
    "I": 7.18,
    "S": 6.59,
    "R": 6.03,
    "H": 5.14,
    "L": 4.03,
    "D": 3.65,
    "C": 3.2,
    "U": 3.1,
    "P": 2.29,
    "F": 2.28,
    "M": 2.25,
    "W": 2.03,
    "Y": 1.88,
    "B": 1.62,
    "G": 1.61,
    "V": 0.93,
    "K": 0.52,
    "X": 0.2,
    "Q": 0.2,
    "J": 0.1,
    "Z": 0.09,
}
occur = {}
dist = {}
results = []

for key in range(0, 26):
    occur = {}
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted = chr((ord(char) - base - key) % 26 + base)
            plaintext += decrypted
            upper_decrypted = decrypted.upper()
            if upper_decrypted in occur:
                occur[upper_decrypted] += 1
            else:
                occur[upper_decrypted] = 1
        else:
            plaintext += char
    plain.append(plaintext)
    diff = 0
    total_letters = sum(occur.values())
    for letter in occur:
        occur[letter] = (occur[letter] / total_letters) * 100 if total_letters > 0 else 0
    for o in sorted(occur.items(), key=lambda x: x[1], reverse=True):
        diff += (o[1] - occ_dict.get(o[0], 0)) ** 2
    dist[key] = diff
    is_meaningful = not nonsense(plaintext.upper())
    results.append((is_meaningful, dist[key], key, plaintext))
    plaintext = ""

meaningful_results = sorted([r for r in results if r[0]], key=lambda x: x[1])
non_meaningful_results = sorted([r for r in results if not r[0]], key=lambda x: x[1])

for is_meaningful, mismatch, key, text in meaningful_results:
    print(
        f"\033[92mKey: {key} - Mismatch: {mismatch} - Meaningful: True\n"
        f"\033[97m{text}\n"
    )

for is_meaningful, mismatch, key, text in non_meaningful_results:
    print(
        f"\033[91mKey: {key} - Mismatch: {mismatch} - Meaningful: False\n"
        f"\033[97m{text}\n"
    )

if meaningful_results:
    best_key, best_plaintext, best_mismatch = meaningful_results[0][2], meaningful_results[0][3], meaningful_results[0][1]
else:
    best_key, best_plaintext, best_mismatch = non_meaningful_results[0][2], non_meaningful_results[0][3], non_meaningful_results[0][1]
    print("\033[93mWarning: No meaningful plaintext found. Using lowest mismatch instead.\033[97m")

with open("../Text/caesar_plaintext.txt", "w", encoding="utf-8") as outfile:
    outfile.write(best_plaintext)

print(
    f"\033[96mSelected plaintext written to caesar_plaintext.txt: "
    f"\033[95m(Key: {best_key}, Mismatch: {best_mismatch})\n"
    f"\033[97m{best_plaintext}"
)