import re

# possui 8 dígitos
# 1º - região / 2º - sub-região / 3º - setor / 4º - subsetor / 5º - divisor do subsetor
# 6-8º - identificadores de sistribuição (sufixo)

lista = [[(1000, 5999), (8000, 8499)], [(6000, 7999), (8500, 9999)]],[[(11000, 11999)], [(12000, 19999)]]
def validacao_cep(lista_cep: list):

    faixa_de_cep = {
                    '0': {
                        'intervalo': [(1000, 5999), (8000, 8499), (6000, 7999), (8500, 9999)],
                        'local': ['São Paulo', 'SP Região metropolitana']
                        },
                    '1': {
                        'intervalo': [(), ()],
                        'local': []
                        },
                    '2': {
                        'intervalo': [],
                        'local': []
                        }
                    }

    regiao_postais = {'0': ['SP - CAPITAL'],
                  '1': ['SP - INTERIOR'],
                  '2': ['RJ', 'ES'],
                  '3': ['MG'],
                  '4': ['BA', 'SE'],
                  '5': ['PE', 'AL', 'PB', 'RN'],
                  '6': ['CE', 'PI', 'MA', 'PA', 'AP', 'AM', 'RR', 'AC'],
                  '7': ['DF', 'GO', 'RO', 'TO', 'MT', 'MS'],
                  '8': ['PR', 'SC'],
                  '9': ['RS']}


    exp_cep = re.findall('\d{5}-\d{3}', lista_cep)
    for cep_encontrado in exp_cep:
        if cep_encontrado[0] in regiao_postais.keys():
            print(cep_encontrado, regiao_postais[f'{cep_encontrado[0]}'])


conjunto_cep = ''''
Nome1: pedro
cep: 02468-000
Nome2 pedro
cep2: 12345-000
Nome3: pedro
cep3: 54321-000
'''

exp_cep = re.findall('\d{5}-\d{3}', conjunto_cep)
# print(exp_cep)

# validacao_cep(conjunto_cep)


sub_regioes = {}
setor = {}
sub_setor = {}
divisor_sub_setor = {}

[ , , '']

regiao_postais = {'0': [[1000, 5999, 'São Paulo'], 
                        [8000, 8499, 'São Paulo'], 
                        [6000, 7999, 'SP Região Metropolitana de São Paulo'], 
                        [8500, 9999, 'SP Região Metropolitana de São Paulo']],
                '1': [[1000, 1999, 'São Paulo Litoral'], 
                      [2000, 9999, 'São Paulo Interior']],
                '2': [[0000, 3799, 'Rio de Janeiro'], 
                      [3800, 6599, 'RJ Região Metropolitana do Rio de Janeiro'], 
                      [6600, 8999, 'RJ Interior'], 
                      [9000, 9099, 'Vitória'], 
                      [9100, 9199, 'ES Região Metropolitana de Vitória'], 
                      [9200, 9999, 'ES Interior']],
                '3': [[0000, 3799, 'Belo Horizonte'], 
                      [3800, 6599, 'MG Região Metropolitana de Belo Horizonte'], 
                      [6600, 8999, 'MG Interior']],
                '4': ['BA', 'SE'],
                '5': ['PE', 'AL', 'PB', 'RN'],
                '6': ['CE', 'PI', 'MA', 'PA', 'AP', 'AM', 'RR', 'AC'],
                '7': ['DF', 'GO', 'RO', 'TO', 'MT', 'MS'],
                '8': ['PR', 'SC'],
                '9': ['RS']}

teste = '01468-000 12345-000'
teste_exp_cep = re.findall('\d{5}-\d{3}', teste)
for cep in teste_exp_cep:
    rpZonaPostal = int(cep[0])
    rpFaixaCep = int(cep[1:5])
    rpConjDados = regiao_postais[f'{rpZonaPostal}']
    for conj in rpConjDados:
        menor = conj[0]
        maior = conj[1]
        if menor <= rpFaixaCep and rpFaixaCep <= maior:
            print(f'A faixa se encontra entre {menor} e {maior} - faixa {rpFaixaCep}')
            print('local', conj[2])
            break
        else:
            print('outro')
        
        

# print(regiao_postais.keys())
