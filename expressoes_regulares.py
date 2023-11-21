"""
Expressões regulares SÃO PADRÕES de caracateres utilizados para buscar, 
analisar e manipular texto. Elas oferecem uma maneira concisa e poderosa 
de descrever conjuntos de cadeias de caracteres, facilitando a validação 
ou extração de informações especificas em textos.

METACARACTERES
    . - Qualquer caractere (exceto linha nova);
    \w - Qualquer caractere alfanumérico;
    \W — qualquer caractere não-alfanumérico;
    \d — Qualquer caractere que seja um dígito (0-9);
    \D - Qualquer caractere não dígito;
    \s — Espaço em branco;
    ^ - começa com;
    $ - termina com;
    "\" — usado antes de metacaracteres para especificar seu significado literal;

QUANTIFICADORES
    [] — opcional entre os que estão dentro dos colchetes;
    ( ) — captura grupos de caracteres;
    * - de zero a mais vezes;
    ? - zero ou uma vez;
    + - uma ou mais vezes;
    {m,n} — de m a n vezes;
    | - ou;
"""

import re


"""
    função search
"""
frase1 = 'Olá, meu número de telefone é (10)00000-0000'
exp_celular_search = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase1)
print(exp_celular_search)

frase2 = 'A placa de carro que eu anotei durante o acidente foi BRA2A19'
exp_placa_search = re.search('[A-Za-z]{3}\d{1}[A-Za-z]{1}\d{2}', frase2)
print(exp_placa_search)

frase3 = 'Entre em contato, meu email é teste@teste.com'
exp_email_search = re.search('\w+@\w+\.com', frase3)
print(exp_email_search)


"""
    função match
"""
frase4 = 'BRA2A19 é a placa do carro'
exp_placa_match = re.match('[A-Za-z]{3}\d{1}[A-Za-z]{1}\d{2}', frase4)
print(exp_placa_match)


"""
    função findall
"""
frase5 = 'Meu número de telefone atual é (11)0000-0000. O número (22)1111-1111 é o antigo'
exp_celular_findall = re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase5)
print(exp_celular_findall)

emails = '''nome: teste1
email: gabrielcosta@hotmail.com
nome: teste2
email: felipearruda@gmail.com
nome: teste3
email: joaosilva@yahoo.com.br'''

exp_email_findall = re.findall('\w+@\w+\.\w*', emails)
print(exp_email_findall)
