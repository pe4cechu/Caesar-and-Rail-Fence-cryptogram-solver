import enchant
from nostril import nonsense

d = enchant.Dict("en_US")


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


def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as infile:
        return infile.read()


def write_file(file_path: str, content: str) -> None:
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(content)


def is_meaningful_dict(text: str, threshold: float = 0.03) -> bool:
    words = [w for w in text.split() if w.isalpha()]
    if not words:
        return False
    non_dict_words = sum(1 for w in words if not d.check(w))
    gibberish_ratio = non_dict_words / len(words)
    return gibberish_ratio <= threshold


def rail_fence_crack(ciphertext: str, max_key: int = 9999):
    thresholds = [
        0.01,
        0.015,
        0.02,
        0.025,
        0.03,
        0.035,
        0.04,
        0.05,
        0.06,
        0.08,
        0.10,
        0.12,
        0.15,
    ]

    for threshold in thresholds:
        results = []
        for key in range(1, max_key + 1):
            plaintext = rail_fence_decrypt(ciphertext, key)
            if not nonsense(plaintext.upper()):
                is_meaningful = is_meaningful_dict(plaintext, threshold=threshold)
            else:
                is_meaningful = False
            results.append((is_meaningful, key, plaintext))
            if is_meaningful:
                break

        meaningful_results = [r for r in results if r[0]]
        non_meaningful_results = [r for r in results if not r[0]]
        if meaningful_results:
            best_key, best_plaintext = (
                meaningful_results[0][1],
                meaningful_results[0][2],
            )
            return meaningful_results, non_meaningful_results, best_key, best_plaintext

    threshold = thresholds[-1]
    results = []
    for key in range(1, max_key + 1):
        plaintext = rail_fence_decrypt(ciphertext, key)
        if not nonsense(plaintext.upper()):
            is_meaningful = is_meaningful_dict(plaintext, threshold=threshold)
        else:
            is_meaningful = False
        results.append((is_meaningful, key, plaintext))
    meaningful_results = [r for r in results if r[0]]
    non_meaningful_results = [r for r in results if not r[0]]
    if meaningful_results:
        best_key, best_plaintext = meaningful_results[0][1], meaningful_results[0][2]
    else:
        best_key, best_plaintext = (
            non_meaningful_results[0][1],
            non_meaningful_results[0][2],
        )
    return meaningful_results, non_meaningful_results, best_key, best_plaintext


def main():
    input_path = "../Text/railfence_ciphertext.txt"
    output_path = "../Text/railfence_plaintext.txt"

    ciphertext = read_file(input_path)
    meaningful_results, non_meaningful_results, best_key, best_plaintext = (
        rail_fence_crack(ciphertext, max_key=9999)
    )

    # print("=== MEANINGFUL CANDIDATES ===")
    # for is_meaningful, key, text in meaningful_results:
    #     print(f"\033[92mKey: {key} - Meaningful: True\n" f"\033[97m{text}\n")
    #
    # print("=== NON-MEANINGFUL CANDIDATES ===")
    # for is_meaningful, key, text in non_meaningful_results:
    #     print(f"\033[91mKey: {key} - Meaningful: False\n" f"\033[97m{text}\n")

    if not meaningful_results:
        print("\033[93mWarning: No meaningful plaintext found.\033[97m")

    write_file(output_path, best_plaintext)
    print(
        f"\033[96mSelected plaintext written to {output_path}: "
        f"\033[95m(Key: {best_key})\n"
        f"\033[97m{best_plaintext}"
    )


if __name__ == "__main__":
    main()
