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
    meaningful_results, non_meaningful_results, best_key, best_plaintext, output_path
):
    print("=== MEANINGFUL CANDIDATES ===")
    for is_meaningful, key, text in meaningful_results:
        print(f"\033[92mKey: {key} - Meaningful: True\n" f"\033[97m{text}\n")

    print("=== NON-MEANINGFUL CANDIDATES ===")
    for is_meaningful, key, text in non_meaningful_results:
        print(f"\033[91mKey: {key} - Meaningful: False\n" f"\033[97m{text}\n")

    if not meaningful_results:
        print("\033[93mWarning: No meaningful plaintext found.\033[97m")

    write_file(output_path, best_plaintext)
    print(
        f"\033[96mSelected plaintext written to {output_path}: "
        f"\033[95m(Key: {best_key})\n"
        f"\033[97m{best_plaintext}"
    )


def print_plaintext_no_key_with_mismatch(
    meaningful_results,
    non_meaningful_results,
    best_key,
    best_mismatch,
    best_plaintext,
    output_path,
):
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

    if not meaningful_results:
        print(
            "\033[93mWarning: No meaningful plaintext found. Using lowest mismatch instead.\033[97m"
        )

    with open(f"{output_path}.txt", "w", encoding="utf-8") as outfile:
        outfile.write(best_plaintext)

    print(
        f"\033[96mSelected plaintext written to {output_path}.txt: "
        f"\033[95m(Key: {best_key}, Mismatch: {best_mismatch})\n"
        f"\033[97m{best_plaintext}"
    )
