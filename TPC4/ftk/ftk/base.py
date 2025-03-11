import re
import json
from collections import Counter
import jjcli  # type: ignore
from ftk.spacy import frequency


def lexer(txt):
    pattern = re.compile(
        r"(?P<WORD>[A-Za-z]+(?:-[A-Za-z]+)*)"  # Words: letters, optionally hyphenated
        r"|(?P<NUMBER>\d+(?:\.\d+)?)"  # Numbers: integer or decimal
        r"|(?P<PUNCT>[^\w\s])"  # Punctuation: non-word, non-space characters
    )
    
    words = [match.group("WORD") for match in pattern.finditer(txt) if match.group("WORD")]
    return words


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def compute_frequencies(text):
    words = lexer(text)
    return Counter(words)


def compare_frequencies(reference_counter, input_counter):
    proportion = {}
    total_reference = sum(reference_counter.values())
    total_input = sum(input_counter.values())
    
    for word in input_counter:
        ref_freq = reference_counter[word] / total_reference if total_reference > 0 else 0
        input_freq = input_counter[word] / total_input if total_input > 0 else 0
        
        proportion[word] = input_freq / ref_freq if ref_freq > 0 else float("inf")
    
    return proportion


def main():
    cl = jjcli.clfilter(opt="f:arpjm:", man=__doc__)
    
    if "-f" not in cl.opt:
        print("Error: You must specify a reference file with -f <file>")
        return
    
    reference_file = cl.opt["-f"]
    reference_text = read_file(reference_file)
    reference_counter = compute_frequencies(reference_text)
    
    for txt in cl.text():
        input_counter = compute_frequencies(txt)
        absolute_freq = frequency.absolute(input_counter)
        relative_freq = frequency.relative(input_counter)
        per_million_freq = frequency.per_million(input_counter)
        proportions = compare_frequencies(reference_counter, input_counter)
        
        if "-a" in cl.opt:
            print("Absolute frequency:")
            for tok, freq in absolute_freq.items():
                print(f"{tok}: {freq}")
        
        if "-r" in cl.opt:
            print("Relative frequency:")
            for tok, freq in relative_freq.items():
                print(f"{tok}: {freq}")
        
        if "-p" in cl.opt:
            print("Per million frequency:")
            for tok, freq in per_million_freq.items():
                print(f"{tok}: {freq}")
        
        if "-j" in cl.opt:
            print(json.dumps(proportions, indent=4))


if __name__ == "__main__":
    main()
