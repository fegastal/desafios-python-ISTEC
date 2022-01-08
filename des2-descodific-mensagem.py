import re
import operator

dicionario = {'O 1': ['4643seattle789915'],
              '. 1': ['18777tel aviv52203'],
              ' 1': ['88147chennai924615'],
              'T 1': ['101439ithaca886154'],
              'Y': ['116529bangalore581853'],
              'D': ['120944mia316713mi'],
              'E 1': ['143960dalla480897s'],
              'X': ['243948sydney563280'],
              'H 1': ['314143sao paulo921914'],
              'I 1': ['335063bueno134720s aires'],
              'E 2': ['357101seoul8920'],
              'C': ['423353edinbrugh748123'],
              ' 2': ['427894shangha848062i'],
              ' 3': ['433015san diego172151'],
              'H 2': ['454933colomb162391o'],
              'I': ['505415mad135226rid'],
              'H 3': ['506350pu80644ne'],
              'N 2': ['524012cairo120796'],
              'O 2': ['594150s239545unnyvale'],
              '.': ['596439jacksonvi594962lle'],
              'E 3': ['609685bristol355981'],
              'E 4': ['622168a713439ustin'],
              'S 1': ['633596hyderaba182478d'],
              'S 2': ['672324barcelona355464'],
              ' 4': ['710866bei287961jing'],
              'E 5': ['713248i896841stanbul'],
              'T 3': ['727652chic786039ago'],
              'S': ['736563s968301an jose'],
              ' 5': ['757144bu435337charest'],
              'E 6': ['779801rocheste161250r'],
              'E': ['794464london844257'],
              'O': ['812575hou328716ston'],
              'N': ['825209manches905277ter'],
              'R': ['825805bogo278985ta'],
              'B 2': ['828205kiev961745'],
              'A': ['843347ber912784keley'],
              '  6': ['879875delhi179051'],
              'L': ['941764ga274374inesville'],
              '  7': ['963482ne168405w york'],
              'K': ['978368a584614thens'],
              'B': ['3734598501singapore'],
              'T': ['163115180776oakland'],
              ' ': ['178088565854karachi'],
              'H': ['519542723001los angeles'],
              }

# Tirando os números dos valores
res = {key: [re.sub('\d', '', ele) for ele in val]
       for key, val in dicionario.items()}
print(res)

# Ordenando os valores em ordem alfabética
sortedDict = sorted(res.items(), key=operator.itemgetter(1))
print(sortedDict)

# Imprimir apenas as chaves para formar a nova frase
for key in sortedDict:
    print(key)

# A frase descodificada é:
# KEYS ARE IN THE CLOSET BEHIND THE SHOE BOX