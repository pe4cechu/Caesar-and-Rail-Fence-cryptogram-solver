from math import sqrt
from nostril import nonsense

with open("../Encryptor/caesar_ciphertext.txt", "r", encoding="utf-8") as infile:
    cipher = infile.read()

temp = ""
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
    for char_old in cipher:
        if char_old.isupper():
            if 65 <= ord(char_old) <= 90:
                char_new = chr((ord(char_old) - 65 + key) % 26 + 65)
                occur[char_new] = occur.get(char_new, 0) + 1
            else:
                char_new = char_old
        elif char_old.islower():
            if 97 <= ord(char_old) <= 122:
                char_new = chr((ord(char_old) - 97 + key) % 26 + 97)
                occur[chr(ord(char_new) - 32)] = occur.get(chr(ord(char_new) - 32), 0) + 1
            else:
                char_new = char_old
        else:
            char_new = char_old
        temp += char_new
    plain.append(temp)
    diff = 0
    for o in sorted(occur.items(), key=lambda x: x[1], reverse=True):
        diff += (o[1] - occ_dict.get(o[0], 0)) ** 2
    dist[key] = sqrt(diff)
    is_meaningful = not nonsense(temp.upper())
    results.append((is_meaningful, dist[key], key, temp))
    temp = ""
    occur = {}

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

with open("caesar_plaintext.txt", "w", encoding="utf-8") as outfile:
    outfile.write(best_plaintext)

print(
    f"\033[96mSelected plaintext written to caesar_plaintext.txt: "
    f"\033[95m(Key: {best_key}, Mismatch: {best_mismatch})\n"
    f"\033[97m{best_plaintext}"
)