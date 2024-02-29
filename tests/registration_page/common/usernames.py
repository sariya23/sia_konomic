from string import punctuation
import random

cyrilic = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"

incorrect_usernames = (
    "a",
    "ab",
    "abo",
    "abob",
    "aboba",
    "a" * 33,
    "7aboba",
    *[f"abo{symbol}ba" for symbol in punctuation if symbol != '_'],
    *["".join(random.sample(cyrilic, word_len)) for word_len in range(6, 33)]
)
