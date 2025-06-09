import enchant

d = enchant.Dict("en_US")


def is_meaningful_dict(text: str, threshold: float) -> bool:
    words = [w for w in text.split() if w.isalpha()]
    if not words:
        return False
    non_dict_words = sum(1 for w in words if not d.check(w))
    gibberish_ratio = non_dict_words / len(words)
    return gibberish_ratio <= threshold
