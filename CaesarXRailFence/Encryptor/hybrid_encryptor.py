from Utils.io import read_file, key_input, print_ciphertext
from Caesar.Encryptor.caesar_encryptor import caesar_encrypt
from RailFence.Encryptor.railfence_encryptor import rail_fence_encrypt


def main():
    input_path = "../../plaintext.txt"
    output_path = "../Text/hybrid_ciphertext.txt"

    plaintext = read_file(input_path)
    key = key_input()
    ciphertext = rail_fence_encrypt(caesar_encrypt(plaintext, key), key)

    print_ciphertext(ciphertext, output_path)


if __name__ == "__main__":
    main()
