def count_vowels(s):
    vowels = "aeiouаеёиоуыэюя"
    if s == "":
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:]
