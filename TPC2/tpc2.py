#!/usr/bin/env python
'''
Repetidas - Remove linhas repetidas de um programa.

Usage -
    repetidas options file*

Options -
    -s      keep spaces 
    -e      remove duplicated empty lines
    -p "#"  adds prefix to the left side of duplicated lines
'''

from jjcli import * # type: ignore

def main():
    cl = clfilter(opt="sep:", man=__doc__) # type: ignore

    different_lines = set()
    result = ""

    for line in cl.input():
        stripped_line = line.rstrip("\n")

        if "-s" in cl.opt: 
            ln = stripped_line
        else:
            ln = stripped_line.strip() # remover espaços à frente e atrás
        
        if ln in different_lines:
            # Adicionar prefixo se -p estiver presente
            if "-p" in cl.opt:
                prefix = cl.opt["-p"]
                result += prefix + ln + "\n"
            
            if not ln and "-e" not in cl.opt: # manter duplicated empty lines
                result += ln + "\n"
                
        else:
            different_lines.add(ln)
            result += ln + "\n"
            
    print(result)

if __name__ == "__main__": #qnd isto está a ser usado como modulo não executar (ig?)
    main()
