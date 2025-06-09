from Utils.io import read_file, key_input, print_plaintext
from Caesar.Decryptor.caesar_decryptor import caesar_decrypt
from RailFence.Decryptor.railfence_decryptor import rail_fence_decrypt


def main():
    input_path = "../Text/hybrid_ciphertext.txt"
    output_path = "../Text/hybrid_plaintext.txt"

    ciphertext = read_file(input_path)
    key = key_input()
    plaintext = caesar_decrypt(rail_fence_decrypt(ciphertext, key), key)

    print_plaintext(plaintext, output_path)


if __name__ == "__main__":
    main()
