def rail_fence_decrypt(ciphertext: str, num_rails: int) -> str:
    if num_rails <= 1 or num_rails >= len(ciphertext):
        return ciphertext
    pattern = [0] * len(ciphertext)
    rail, direction = 0, 1
    for i in range(len(ciphertext)):
        pattern[i] = rail
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction
    rail_counts = [pattern.count(r) for r in range(num_rails)]
    rails = []
    idx = 0
    for count in rail_counts:
        rails.append(list(ciphertext[idx:idx+count]))
        idx += count
    result = []
    rail_indices = [0] * num_rails
    for r in pattern:
        result.append(rails[r][rail_indices[r]])
        rail_indices[r] += 1
    return ''.join(result)

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as infile:
        return infile.read()

def write_file(file_path: str, content: str) -> None:
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(content)

def main():
    input_path = "../Text/rail_fence_ciphertext.txt"
    output_path = "../Text/rail_fence_plaintext.txt"
    ciphertext = read_file(input_path)
    try:
        key = int(input("Enter a key: "))
    except ValueError:
        print("\033[91mInvalid key. Please enter a valid integer.\033[97m")
        return
    plaintext = rail_fence_decrypt(ciphertext, key)
    print("\033[92m\nDecrypted plaintext:")
    print(f"\033[97m{plaintext}")
    write_file(output_path, plaintext)
    print(f"\033[96m\nPlaintext written to {output_path}\033[97m")

if __name__ == "__main__":
    main()