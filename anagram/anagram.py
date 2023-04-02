def find_anagrams(word: str, candidates: list[str]):
    return [i for i in candidates if sorted(word.lower()) == sorted(i.lower()) and word.lower() != i.lower()]

