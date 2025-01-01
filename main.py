from collections import defaultdict
from typing import Dict

def get_wordcount_int(string: str) -> int:
    return len(string.split())

def get_charcount_dict(string: str) -> Dict[str, int]:
    result: Dict[str, int] = defaultdict(int)
    for char in string:
        lowerchar = char.lower()
        result[lowerchar] += 1
    return result
        

def main(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    wc: int = get_wordcount_int(file_contents)
    cc: Dict[str, int] = get_charcount_dict(file_contents)
    cc_sorted: Dict[str, int] = dict(sorted(cc.items(), key=lambda item: item[1], reverse=True))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document\n\n")
    for i in cc_sorted:
        if (i.isalpha()):
            print(f"The '{i}' character was found {cc[i]} times.")

    print("--- End report ---")


main("books/frankenstein.txt")