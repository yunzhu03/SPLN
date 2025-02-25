## TPC1:

### 2025-02-11

## Resumo
Continuação do TPC1 com adição de linhas de comando. 
Utilização da biblioteca jjcli.

    -s          keep spaces
    -e          remove duplicated empty lines
    -p "#"      prefixo, às linhas repetidas adicionar um cardinal

### Execução
```
chmod +x tpc1.py
./tpc1.py -s exemplo.txt
./tpc1.py -e exemplo.txt
./tpc1.py -p "Olé" exemplo.txt
./tpc1.py -s -e -p "$" exemplo.txt
```

## Resolução
Adaptação do exemplo da aula.