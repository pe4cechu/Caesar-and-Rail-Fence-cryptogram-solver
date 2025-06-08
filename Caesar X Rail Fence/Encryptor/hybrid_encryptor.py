from Caesar.Encryptor.caesar_encryptor import caesar_encrypt
from RailFence.Encryptor.railfence_encryptor import rail_fence_encrypt


def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as infile:
        return infile.read()


def write_file(file_path: str, text: str) -> None:
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(text)


def main():
    input_path = "../../plaintext.txt"
    output_path = "../Text/hybrid_ciphertext.txt"

    plaintext = read_file(input_path)

    try:
        key = int(input("Enter a key: "))
    except ValueError:
        print("\033[91mInvalid key. Please enter an integer.\033[97m")
        return

    ciphertext = rail_fence_encrypt(caesar_encrypt(plaintext, key), key)

    print("\033[92m\nEncrypted ciphertext:")
    print(f"\033[97m{ciphertext}")

    write_file(output_path, ciphertext)

    print("\033[96m\nCiphertext written to hybrid_ciphertext.txt\033[97m")


if __name__ == "__main__":
    main()
