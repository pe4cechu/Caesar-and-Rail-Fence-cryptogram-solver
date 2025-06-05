def rail_fence_encrypt(text: str, num_rails: int) -> str:
    if num_rails <= 1 or num_rails >= len(text):
        return text
    rails = ['' for _ in range(num_rails)]
    rail = 0
    direction = 1
    for char in text:
        rails[rail] += char
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction
    return ''.join(rails)

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as infile:
        return infile.read()

def write_file(file_path: str, content: str) -> None:
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(content)

def main():
    input_path = "../../plaintext.txt"
    output_path = "../Text/rail_fence_ciphertext.txt"
    plaintext = read_file(input_path)
    try:
        key = int(input("Enter a key: "))
    except ValueError:
        print("\033[91mInvalid key. Please enter a valid integer.\033[97m")
        return
    ciphertext = rail_fence_encrypt(plaintext, key)
    print("\033[92m\nCiphertext:\033[97m")
    print(ciphertext)
    write_file(output_path, ciphertext)
    print(f"\033[96m\nCiphertext written to {output_path}\033[97m")

if __name__ == "__main__":
    main()