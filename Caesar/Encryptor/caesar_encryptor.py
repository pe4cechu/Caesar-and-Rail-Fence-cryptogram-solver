from Utils.io import read_file, key_input, print_ciphertext


def caesar_encrypt(plaintext: str, shift: int) -> str:
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def main():
    input_path = "../../plaintext.txt"
    output_path = "../Text/caesar_ciphertext.txt"

    plaintext = read_file(input_path)
    key = key_input()
    ciphertext = caesar_encrypt(plaintext, key)

    print_ciphertext(ciphertext, output_path)


if __name__ == "__main__":
    main()
