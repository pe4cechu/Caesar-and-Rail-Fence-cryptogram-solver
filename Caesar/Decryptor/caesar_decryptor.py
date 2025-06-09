from Utils.io import read_file, key_input, print_plaintext


def caesar_decrypt(ciphertext: str, key: int) -> str:
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            plaintext += chr((ord(char) - base - key) % 26 + base)
        else:
            plaintext += char
    return plaintext


def main():
    input_path = "../Text/caesar_ciphertext.txt"
    output_path = "../Text/caesar_plaintext.txt"

    ciphertext = read_file(input_path)
    key = key_input()
    plaintext = caesar_decrypt(ciphertext, key)

    print_plaintext(plaintext, output_path)


if __name__ == "__main__":
    main()
