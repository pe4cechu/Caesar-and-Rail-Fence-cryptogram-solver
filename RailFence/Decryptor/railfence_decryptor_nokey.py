from nostril import nonsense

from Utils.io import read_file, print_plaintext_no_key
from Utils.dict import is_meaningful_dict
from RailFence.Decryptor.railfence_decryptor import rail_fence_decrypt


def rail_fence_crack(ciphertext: str, max_key: int = 9999):
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

    results = []
    for th in thresholds:
        results = []
        for key in range(1, max_key + 1):
            plaintext = rail_fence_decrypt(ciphertext, key)
            if not nonsense(plaintext.upper()):
                is_meaningful, gibberish_ratio = is_meaningful_dict(
                    plaintext, threshold=th
                )
            else:
                is_meaningful, gibberish_ratio = False, None
            results.append(
                (
                    is_meaningful,
                    key,
                    plaintext,
                    round(gibberish_ratio, 4) if gibberish_ratio is not None else None,
                )
            )
            if is_meaningful:
                meaningful_results = [results[-1]]
                non_meaningful_results = results[:-1]
                key, plaintext = key, plaintext
                return meaningful_results, non_meaningful_results, key, plaintext

    meaningful_results = [r for r in results if r[0]]
    non_meaningful_results = [r for r in results if not r[0]]

    if meaningful_results:
        key, plaintext = meaningful_results[0][1], meaningful_results[0][2]
    else:
        key, plaintext = non_meaningful_results[0][1], non_meaningful_results[0][2]
    return meaningful_results, non_meaningful_results, key, plaintext


def main():
    input_path = "../Text/railfence_ciphertext.txt"
    output_path = "../Text/railfence_plaintext.txt"

    ciphertext = read_file(input_path)
    meaningful_results, non_meaningful_results, key, plaintext = rail_fence_crack(
        ciphertext
    )

    print_plaintext_no_key(
        meaningful_results,
        non_meaningful_results,
        key,
        plaintext,
        output_path,
    )


if __name__ == "__main__":
    main()
