def caesar_encrypt(plaintext: str, shift: int) -> str:
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as infile:
        return infile.read()

def write_file(file_path: str, text: str) -> None:
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(text)

def main():
    input_path = "../../plaintext.txt"
    output_path = "../Text/caesar_ciphertext.txt"

    plaintext = read_file(input_path)

    try:
        key = int(input("Enter a key: "))
    except ValueError:
        print("\033[91mInvalid key. Please enter an integer.\033[97m")
        return

    ciphertext = caesar_encrypt(plaintext, key)

    print("\033[92m\nEncrypted ciphertext:")
    print(f"\033[97m{ciphertext}")

    write_file(output_path, ciphertext)

    print("\033[96m\nCiphertext written to caesar_ciphertext.txt\033[97m")

if __name__ == "__main__":
    main()