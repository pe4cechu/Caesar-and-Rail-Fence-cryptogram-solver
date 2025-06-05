def caesar_decrypt(ciphertext: str, shift: int) -> str:
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted = chr((ord(char) - base - shift) % 26 + base)
            plaintext += decrypted
        else:
            plaintext += char
    return plaintext

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as infile:
        return infile.read()

def write_file(file_path: str, text: str) -> None:
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(text)

def main():
    input_path = "../Text/caesar_ciphertext.txt"
    output_path = "../Text/caesar_plaintext.txt"

    ciphertext = read_file(input_path)

    try:
        key = int(input("Enter the decryption key (shift): "))
    except ValueError:
        print("\033[91mInvalid key. Please enter an integer.\033[97m")
        return

    plaintext = caesar_decrypt(ciphertext, key)

    print("\033[92m\nDecrypted plaintext:")
    print(f"\033[97m{plaintext}")

    write_file(output_path, plaintext)

    print("\033[96m\nPlaintext written to caesar_plaintext.txt\033[97m")

if __name__ == "__main__":
    main()