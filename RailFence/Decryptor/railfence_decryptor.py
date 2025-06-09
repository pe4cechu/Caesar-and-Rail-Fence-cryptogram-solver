from Utils.io import read_file, key_input, print_plaintext


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
        rails.append(list(ciphertext[idx : idx + count]))
        idx += count
    result = []
    rail_indices = [0] * num_rails
    for r in pattern:
        result.append(rails[r][rail_indices[r]])
        rail_indices[r] += 1
    return "".join(result)


def main():
    input_path = "../Text/railfence_ciphertext.txt"
    output_path = "../Text/railfence_plaintext.txt"

    ciphertext = read_file(input_path)
    key = key_input()
    plaintext = rail_fence_decrypt(ciphertext, key)

    print_plaintext(plaintext, output_path)


if __name__ == "__main__":
    main()
