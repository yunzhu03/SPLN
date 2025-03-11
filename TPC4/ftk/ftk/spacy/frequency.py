from collections import Counter

def absolute(counter):
    res = {}
    for token, count in counter.items():
        res[token] = count
    return res
        

def relative(counter):
    res = {}
    for token, count in counter.items():
        res[token] = count/ len(counter)
    return res

def per_million(counter):
    res = {}
    for token, count in counter.items():
        res[token] = count/ len(counter)
        (count / len(counter)) * 1000000
    return res

def ratio(rel1, rel2):
    res = {}
    r2 = dict(rel2)
    for word, count in rel1:
        res[word] = count / r2.get(word,1/1000000)
    return res

def ratio(counter1, counter2):
    common = set(counter1.keys()) & set(counter2.keys())  # Find common words
    return {word: min(counter1[word], counter2[word]) / max(counter1[word], counter2[word]) for word in common}

    