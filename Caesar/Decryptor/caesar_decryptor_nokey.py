from nostril import nonsense
from Utils.io import read_file, print_plaintext_no_key_with_mismatch
from Utils.dict import is_meaningful_dict

def frequency_profile():
    return {
        "A": 8.167,
        "B": 1.492,
        "C": 2.782,
        "D": 4.253,
        "E": 12.702,
        "F": 2.228,
        "G": 2.015,
        "H": 6.094,
        "I": 6.966,
        "J": 0.153,
        "K": 0.772,
        "L": 4.025,
        "M": 2.406,
        "N": 6.749,
        "O": 7.507,
        "P": 1.929,
        "Q": 0.095,
        "R": 5.987,
        "S": 6.327,
        "T": 9.056,
        "U": 2.758,
        "V": 0.978,
        "W": 2.360,
        "X": 0.150,
        "Y": 1.974,
        "Z": 0.074,
    }

def caesar_decrypt(ciphertext: str, key: int) -> str:
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            plaintext += chr((ord(char) - base - key) % 26 + base)
        else:
            plaintext += char
    return plaintext

def letter_occurrence(text: str) -> dict:
    occur = {}
    for char in text:
        if char.isalpha():
            upper_char = char.upper()
            occur[upper_char] = occur.get(upper_char, 0) + 1
    total = sum(occur.values())
    for letter in occur:
        occur[letter] = (occur[letter] / total) * 100 if total > 0 else 0
    return occur

def frequency_distance(occ: dict, profile: dict) -> float:
    diff = 0
    for letter, freq in occ.items():
        diff += (freq - profile.get(letter, 0)) ** 2
    return diff

def caesar_crack(ciphertext: str):
    occ_dict = frequency_profile()
    results = []
    for key in range(26):
        plaintext = caesar_decrypt(ciphertext, key)
        occur = letter_occurrence(plaintext)
        diff = frequency_distance(occur, occ_dict)
        if not nonsense(plaintext.upper()):
            is_meaningful, gibberish_ratio = is_meaningful_dict(
                plaintext, threshold=1
            )
        else:
            is_meaningful, gibberish_ratio = False, None
        results.append((
            is_meaningful,
            round(diff, 4),
            key,
            plaintext,
            round(gibberish_ratio, 4) if gibberish_ratio is not None else None,
        ))
    meaningful_results = [r for r in results if r[0]]
    non_meaningful_results = [r for r in results if not r[0]]
    if meaningful_results:
        best_result = meaningful_results[0]
    else:
        best_result = non_meaningful_results[0] if non_meaningful_results else (None, None, None, None, None)
    _, mismatch, key, plaintext, gibberish_ratio = best_result
    return (
        meaningful_results,
        non_meaningful_results,
        key,
        plaintext,
        gibberish_ratio,
        mismatch,
    )

def main():
    input_path = "../Text/caesar_ciphertext.txt"
    output_path = "../Text/caesar_plaintext.txt"
    ciphertext = read_file(input_path)
    (
        meaningful_results,
        non_meaningful_results,
        key,
        plaintext,
        gibberish_ratio,
        mismatch,
    ) = caesar_crack(ciphertext)
    print_plaintext_no_key_with_mismatch(
        meaningful_results,
        non_meaningful_results,
        key,
        mismatch,
        plaintext,
        output_path,
    )

if __name__ == "__main__":
    main()