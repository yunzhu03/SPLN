## TPC5: separar em tabela PT-TT, e para um ficheiro a parte o que for unknown

## Complementar: fazer sistema de reescrita textual

```
def a(t):
    the   ==> o
    cat   ==> gato
    (\w+) =e=> lambda x: dicionario.get(x[1],x[1])

def transform_a(t):
    t = re.sub(r'\bthe\b','o',t)
    t = re.sub(r'\bgato\b','gato',t)
    t = re.sub(r'\b(\w+)\b',lambda x: dicionario.get(x[1],x[1]),t)
    return t
```

tentativa (dsl)
