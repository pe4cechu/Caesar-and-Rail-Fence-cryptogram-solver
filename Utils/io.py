def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as infile:
        return infile.read()


def write_file(file_path: str, content: str) -> None:
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(content)


def key_input():
    while True:
        try:
            return int(input("Enter the decryption key (shift): "))
        except ValueError:
            print("\033[91mInvalid key. Please enter an integer.\033[97m")


def print_ciphertext(ciphertext, output_path):
    print("\033[92m\nEncrypted ciphertext:")
    print(f"\033[97m{ciphertext}")
    write_file(output_path, ciphertext)
    print(f"\033[96m\nCiphertext written to {output_path}\033[97m")


def print_plaintext(plaintext, output_path):
    print("\033[92m\nDecrypted plaintext:")
    print(f"\033[97m{plaintext}")

    write_file(output_path, plaintext)

    print(f"\033[96m\nPlaintext written to {output_path}\033[97m")


def print_plaintext_no_key(
    meaningful_results, non_meaningful_results, key, plaintext, output_path
):

    print("=== NON-MEANINGFUL CANDIDATES ===")
    for is_meaningful, key, text, ratio in non_meaningful_results:
        print(
            f"\033[91mKey: {key} - False Positive Ratio: {ratio} - Meaningful: False\n"
            f"\033[97m{text}\n"
        )

    print("=== MEANINGFUL CANDIDATES ===")
    for is_meaningful, key, text, ratio in meaningful_results:
        print(
            f"\033[92mKey: {key} - False Positive Ratio: {ratio} - Meaningful: True\n"
            f"\033[97m{text}\n"
        )

    if meaningful_results:
        write_file(output_path, plaintext)
        print(
            f"\033[96mSelected plaintext written to {output_path}: "
            f"\033[95m(Key: {key} - False Positive Ratio: {meaningful_results[0][3]})\n"
            f"\033[97m{plaintext}"
        )
    else:
        print(
            f"\033[96mSelected plaintext written to {output_path}: "
            f"\033[95m(Key: {key} - False Positive Ratio: {non_meaningful_results[0][3]})\n"
            f"\033[97m{plaintext}"
        )


def print_plaintext_no_key_with_mismatch(
    meaningful_results,
    non_meaningful_results,
    key,
    mismatch,
    plaintext,
    output_path,
):
    print("=== NON-MEANINGFUL CANDIDATES ===")
    for is_meaningful, mismatch, key, text, ratio in non_meaningful_results:
        print(
            f"\033[91mKey: {key} - Mismatch: {mismatch} - False Positive Ratio: {ratio} - Meaningful: False\n"
            f"\033[97m{text}\n"
        )

    print("=== MEANINGFUL CANDIDATES ===")
    for is_meaningful, mismatch, key, text, ratio in meaningful_results:
        print(
            f"\033[92mKey: {key} - Mismatch: {mismatch} - False Positive Ratio: {ratio}  - Meaningful: True\n"
            f"\033[97m{text}\n"
        )

    if meaningful_results:
        with open(f"{output_path}", "w", encoding="utf-8") as outfile:
            outfile.write(plaintext)

        print(
            f"\033[96mSelected plaintext written to {output_path}: "
            f"\033[95m(Key: {key}, Mismatch: {mismatch}, False Positive Ratio: {meaningful_results[0][4]})\n"
            f"\033[97m{plaintext}"
        )
    else:
        print("\033[93mWarning: No meaningful plaintext found.\033[97m")