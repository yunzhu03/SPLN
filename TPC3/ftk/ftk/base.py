import re
import jjcli # type: ignore
from collections import Counter

from ftk.spacy import integer, lemma

# def lexer(txt):
#     # FIXME me patters stopwords lems
#     return re.findall(r"\w+(?:-\w+)*|[^\s\w]",txt) #?: significa agrupar só sem capturar

def lexer(txt):
    pattern = re.compile(
        r"(?P<WORD>[A-Za-z]+(?:-[A-Za-z]+)*)"   # words: letters, optionally hyphenated
        r"|(?P<NUMBER>\d+(?:\.\d+)?)"           # numbers: integer or decimal numbers
        r"|(?P<PUNCT>[^\w\s])"                  # punctuation: non-word, non-space characters
    )
    
    words = []
    numbers = []
    punctuation = []
    
    for match in pattern.finditer(txt):
        if match.group("WORD"):
            words.append(match.group("WORD"))
        elif match.group("NUMBER"):
            numbers.append(match.group("NUMBER"))
        elif match.group("PUNCT"):
            punctuation.append(match.group("PUNCT"))
    
    return words, numbers, punctuation

def counter(tokens): 
    return Counter(*tokens)

def main():
    cl = jjcli.clfilter()
    
    word_tokens = []
    number_tokens = []
    punctuation_tokens = []
    
    for txt in cl.text():
        
        word, number, punctuation = lexer(txt)
        word_tokens.append(word) 
        number_tokens.append(number)
        punctuation_tokens.append(punctuation)
        
        print(f"word token: {word}")
        print(counter(word_tokens))
        
        print(f"Number token: {number}")
        print(counter(number_tokens))
        
        print(f"Punctuation token: {punctuation}")
        print(counter(punctuation_tokens))
        
    lemmatized = lemma.lemmatize(word_tokens)     
    word_freqs = integer.compute_frequencies(lemmatized)
    number_freqs = integer.compute_frequencies(number_tokens)
    punctuation_freqs = integer.compute_frequencies(punctuation_tokens)
    
    print("Word Frequencies:", word_freqs)
    print("Number Frequencies:", number_freqs)
    print("Punctuation Frequencies:", punctuation_freqs)
    
if __name__=="__main__":
    main()
    
    