from nostril import nonsense

from Utils.io import read_file, print_plaintext_no_key
from Utils.dict import is_meaningful_dict
from RailFence.Decryptor.railfence_decryptor import rail_fence_decrypt


def rail_fence_crack(ciphertext: str, max_key: int = 99999):
    thresholds = [
        0.01,
        0.015,
        0.02,
        0.025,
        0.03,
        0.035,
        0.04,
        0.05,
        0.06,
        0.08,
        0.10,
        0.12,
        0.15,
    ]

    for threshold in thresholds:
        results = []
        for key in range(1, max_key + 1):
            plaintext = rail_fence_decrypt(ciphertext, key)
            if not nonsense(plaintext.upper()):
                is_meaningful = is_meaningful_dict(plaintext, threshold=threshold)
            else:
                is_meaningful = False
            results.append((is_meaningful, key, plaintext))
            if is_meaningful:
                break

        meaningful_results = [r for r in results if r[0]]
        non_meaningful_results = [r for r in results if not r[0]]
        if meaningful_results:
            best_key, best_plaintext = (
                meaningful_results[0][1],
                meaningful_results[0][2],
            )
            return meaningful_results, non_meaningful_results, best_key, best_plaintext

    threshold = thresholds[-1]
    results = []
    for key in range(1, max_key + 1):
        plaintext = rail_fence_decrypt(ciphertext, key)
        if not nonsense(plaintext.upper()):
            is_meaningful = is_meaningful_dict(plaintext, threshold=threshold)
        else:
            is_meaningful = False
        results.append((is_meaningful, key, plaintext))
    meaningful_results = [r for r in results if r[0]]
    non_meaningful_results = [r for r in results if not r[0]]
    if meaningful_results:
        best_key, best_plaintext = meaningful_results[0][1], meaningful_results[0][2]
    else:
        best_key, best_plaintext = (
            non_meaningful_results[0][1],
            non_meaningful_results[0][2],
        )
    return meaningful_results, non_meaningful_results, best_key, best_plaintext


def main():
    input_path = "../Text/railfence_ciphertext.txt"
    output_path = "../Text/railfence_plaintext.txt"

    ciphertext = read_file(input_path)
    meaningful_results, non_meaningful_results, best_key, best_plaintext = (
        rail_fence_crack(ciphertext, max_key=9999)
    )

    print_plaintext_no_key(
        meaningful_results,
        non_meaningful_results,
        best_key,
        best_plaintext,
        output_path,
    )


if __name__ == "__main__":
    main()
