from lark import Lark, Transformer, v_args, Token
import pandas as pd

# Gramática Lark para reconhecer os dois tipos de definição e conteúdos desconhecidos
grammar = f"""
start: segment+

segment: explicit_def
       | title_def
       | unknown

explicit_def: "PORTUGUÊS:" pt_text "TETUN:" tt_text

title_def: title_line
title_line: /.+?\s*\(.+?\)/  

unknown: unknown_line+
unknown_line: /.+/

pt_text: /.+/
tt_text: /.+/

%import common.WS
%ignore WS

"""

class ExtractTransformer(Transformer):
    def explicit_def(self, items):
        pt_text = str(items[0]).strip()
        tt_text = str(items[1]).strip()
        return ('def', pt_text, tt_text)

    def title_def(self, items):
        title = str(items[0]).strip()
        if "(" in title and ")" in title:
            pt, tt = title.split("(", 1)
            return ('title', pt.strip(), tt.rstrip(")").strip())
        return ('title', title, "")

    def unknown(self, items):
        return ('unknown', "\n".join(str(i) for i in items).strip())

    
    def text_line(self, token):
        if isinstance(token, list):
            return token[0].value
        else:
            return token.value

# Criação do parser Lark
parser = Lark(grammar, parser='earley', maybe_placeholders=False)

# Exemplo de conteúdo do ficheiro (pode ser substituído pela leitura de um arquivo)
texto = """Capa: Leonardo Menezes Melo
Imagens da capa e miolo: Leonardo Menezes Melo

Abscissa (Absisa)
PORTUGUÊS: Localização de um ponto em relação ao eixo horizontal x. Pode ter posição positiva, negativa ou nula.
TETUN: Fatin ba pontu sira-nebé iha relasaun ho eixu orizontál (eixu x). Bele iha pozisaun pozitiva, negativa ou nula.

Acutângulo (Akutángulu)
PORTUGUÊS: Figura geométrica com ângulos agudos ou menores que 90º.
TETUN: Figura jeométrika ho sikun sira agudu ka sikun sira ki liu hosi 90º.
"""


tree = parser.parse(texto)
result = ExtractTransformer().transform(tree)



print(result.pretty())

# df = pd.DataFrame(tabela, columns=["Português", "Tetun"])
# df.to_csv("tabela_PT-TT.csv", index=False, encoding="utf-8")

# with open("unknown.txt", "w", encoding="utf-8") as f:
#     for text in unknown_texts:
#         f.write(text + "\n")
