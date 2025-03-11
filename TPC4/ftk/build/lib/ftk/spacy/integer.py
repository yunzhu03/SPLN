from collections import Counter

def compute_frequencies(tokens):
   
    total_tokens = len(tokens)
    counter = Counter(tokens)
    
    frequencies = {}
    
    for token, count in counter.items():
        frequencies[token] = {
            "absolute_frequency": count,
            "relative_frequency": count / total_tokens,
            "parts_per_million": (count / total_tokens) * 1_000_000
        }
    return frequencies
