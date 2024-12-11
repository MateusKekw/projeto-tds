# https://medium.com/@felipe.odorcyk/web-scrapping-obtendo-resultados-de-partidas-de-diferentes-ligas-do-soccerstats-com-3d2061a0268b

# pip install requests
# pip install lxml
# pip install bs4
# pip install pandas
# pip install openpyxl

import requests
import bs4
import pandas as pd

def baixarbrasileirao():
    site = requests.get(
        'https://www.soccerstats.com/results.asp?league=brazil&pmtype=bydate')

    ss = bs4.BeautifulSoup(site.text, 'lxml')

    dow = []
    dia = []
    mes = []
    time_casa = []
    gls_casa = []
    gls_fora = []
    time_fora = []
    ht_casa = []
    ht_fora = []

    # itera pelas classes e salva o índice final onde ocorrem partidas
    is_match = 0
    while is_match == 0:
        for x in range(len(ss.select('.odd'))):
            if len(ss.select('.odd')[x*(-1)]) != 9:
                is_match = 1
                final = len(ss.select('.odd'))-x
            else:
                pass

    # itera por partidas e pega resultados
    for i in range(final):
        match = ss.select('.odd')[i].text
        spt = match.split()

    # checa se tem nomes de times com espaços
        if len(spt) > 7:

            # checa se o time da casa tem espaço, se tiver substitui por _
            while not spt[3].isnumeric():
                spt[2] = '_'.join(spt[2:4])
                del spt[3]

    # checa se o time de fora tem espaço, se tiver substitui por _
            while not spt[-2].isnumeric():
                spt[-1] = '_'.join(spt[-2:])
                del spt[-2]

        dow.append(spt[0])
        dia.append(spt[1])
        mes.append(spt[2][:3])
        time_casa.append(spt[2][3:])
        gls_casa.append(spt[3])
        gls_fora.append(spt[5])
        time_fora.append(spt[6][0:spt[6].find('(')])
        ht_casa.append(spt[6][-7])
        ht_fora.append(spt[6][-5])

        df = pd.DataFrame(list(zip(dow, dia, mes, time_casa, gls_casa, gls_fora, time_fora, ht_casa, ht_fora)),
                        columns=['dow', 'dia', 'mes', 'time_casa', 'gls_casa', 'gls_fora', 'time_fora', 'ht_casa', 'ht_fora'])

    # df.to_json('brasileirao.json', orient='records', lines=True)
    resultado = df.to_json(orient='records', lines=True)
    return resultado
