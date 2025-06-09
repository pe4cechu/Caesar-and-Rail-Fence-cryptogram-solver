from Utils.io import read_file, key_input, print_ciphertext


def rail_fence_encrypt(text: str, num_rails: int) -> str:
    if num_rails <= 1 or num_rails >= len(text):
        return text
    rails = ["" for _ in range(num_rails)]
    rail = 0
    direction = 1
    for char in text:
        rails[rail] += char
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction
    return "".join(rails)


def main():
    input_path = "../../plaintext.txt"
    output_path = "../Text/railfence_ciphertext.txt"

    plaintext = read_file(input_path)
    key = key_input()
    ciphertext = rail_fence_encrypt(plaintext, key)

    print_ciphertext(ciphertext, output_path)


if __name__ == "__main__":
    main()
