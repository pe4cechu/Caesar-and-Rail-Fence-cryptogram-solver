from nostril import nonsense

from Utils.io import read_file, print_plaintext_no_key_with_mismatch
from Utils.dict import is_meaningful_dict
from Caesar.Decryptor.caesar_decryptor import caesar_decrypt
from Caesar.Decryptor.caesar_decryptor_nokey import (
    frequency_profile,
    letter_occurrence,
    frequency_distance,
)
from RailFence.Decryptor.railfence_decryptor import rail_fence_decrypt


def hybrid_crack(ciphertext: str, max_key: int = 9999):
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

    occ_dict = frequency_profile()
    results = []

    for th in thresholds:
        results = []
        for key in range(1, max_key + 1):
            plaintext = caesar_decrypt(rail_fence_decrypt(ciphertext, key), key)
            occur = letter_occurrence(plaintext)
            diff = frequency_distance(occur, occ_dict)
            if not nonsense(plaintext.upper()):
                is_meaningful, gibberish_ratio = is_meaningful_dict(
                    plaintext, threshold = th
                )
            else:
                is_meaningful, gibberish_ratio = False, None
            results.append(
                (
                    is_meaningful,
                    round(diff, 4),
                    key,
                    plaintext,
                    round(gibberish_ratio, 4) if gibberish_ratio is not None else None,
                )
            )
            meaningful_results = [r for r in results if r[0]]
            non_meaningful_results = [r for r in results if not r[0]]
            if is_meaningful:
                key, plaintext, mismatch = (
                    meaningful_results[0][2],
                    meaningful_results[0][3],
                    meaningful_results[0][1],
                )
                return (
                    meaningful_results,
                    non_meaningful_results,
                    key,
                    plaintext,
                    mismatch,
                )


    meaningful_results = [r for r in results if r[0]]
    non_meaningful_results = [r for r in results if not r[0]]

    if meaningful_results:
        key, plaintext, mismatch = (
            meaningful_results[0][2],
            meaningful_results[0][3],
            meaningful_results[0][1],
        )
    else:
        key, plaintext, mismatch = (
            non_meaningful_results[0][2],
            non_meaningful_results[0][3],
            non_meaningful_results[0][1],
        )
    return (
        meaningful_results,
        non_meaningful_results,
        key,
        plaintext,
        mismatch,
    )



def main():
    input_path = "../Text/hybrid_ciphertext.txt"
    output_path = "../Text/hybrid_plaintext.txt"

    ciphertext = read_file(input_path)
    (
        meaningful_results,
        non_meaningful_results,
        key,
        plaintext,
        mismatch,
    ) = hybrid_crack(ciphertext)

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