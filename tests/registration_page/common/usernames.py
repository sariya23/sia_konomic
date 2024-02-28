from string import punctuation

incorrect_usernames = (
    "",
    "a",
    "ab",
    "abo",
    "abob",
    "aboba",
    "a" * 33,
    "7aboba",
    *[f"abo{symbol}ba" for symbol in punctuation if symbol != '_']
)