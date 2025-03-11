
# Dictionary for irregular words and their lemmas
IRREGULAR_LEMMAS = {
    "ran": "run",
    "running": "run",
    "ate": "eat",
    "eating": "eat",
    "better": "good",
    "worse": "bad",
    "mice": "mouse",
    "geese": "goose",
    "children": "child",
}

def lemmatize_word(word):
    
    if word in IRREGULAR_LEMMAS:
        return IRREGULAR_LEMMAS[word]
    
    # Rule-based lemmatization for simple cases
    if word.endswith("ing") and len(word) > 4:
        return word[:-3]  # e.g., "playing" -> "play"
    if word.endswith("ed") and len(word) > 3:
        return word[:-2]  # e.g., "walked" -> "walk"
    if word.endswith("es") and len(word) > 3:
        return word[:-2]  # e.g., "watches" -> "watch"
    if word.endswith("s") and len(word) > 3:
        return word[:-1]  # e.g., "cars" -> "car"
    
    return word  # Return original if no rules apply

def lemmatize(tokens):
    res = []
    for token in tokens:
        res.append(lemmatize_word(token))
    return res
