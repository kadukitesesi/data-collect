# %% 

import requests
from bs4 import BeautifulSoup


def request_content(name):
    name.lower()
    name.replace(" ", "-")
    url = f'https://www.residentevildatabase.com/personagens/{name}/'

    cookies = {
        '_ga_DJLCSW50SC': 'GS2.1.s1754163975$o1$g1$t1754166223$j42$l0$h0',
        '_ga': 'GA1.2.83934290.1754163975',
        '_ga_D6NF5QC4QT': 'GS2.1.s1754163976$o1$g1$t1754166224$j35$l0$h0',
        '_gid': 'GA1.2.598374792.1754163976',
        '__gads': 'ID=85a79dbdecdfd602:T=1754163992:RT=1754166203:S=ALNI_MbSl7ja4ME7Jh0HcIH72c26aMAgUA',
        '__gpi': 'UID=00001106c99d276d:T=1754163992:RT=1754166203:S=ALNI_MZrXyx8Ww-Gj-HQkMsEep8YutPaig',
        '__eoi': 'ID=99c6d9000ca1b8b8:T=1754163992:RT=1754166203:S=AA-AfjYYyn9nry1Lo0brlspxZ9d9',
        '_gat_gtag_UA_29446588_1': '1',
        'FCNEC': '%5B%5B%22AKsRol-XjIiTS7Q4wt_NgCY4TyEhPnomP5k7N9Q_XN-bCM9LjLBhQ9w-lzUqlxdY4zzACsiZTvZMWajcVQTEuRsrAYv8XGpI1Z-ZYQ2jTq6U2-3CTurk_iYGFiX9whRul-nGFbyyiWfxZfk2fI27pD78Z67o3xYhjg%3D%3D%22%5D%5D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga_DJLCSW50SC=GS2.1.s1754163975$o1$g1$t1754166223$j42$l0$h0; _ga=GA1.2.83934290.1754163975; _ga_D6NF5QC4QT=GS2.1.s1754163976$o1$g1$t1754166224$j35$l0$h0; _gid=GA1.2.598374792.1754163976; __gads=ID=85a79dbdecdfd602:T=1754163992:RT=1754166203:S=ALNI_MbSl7ja4ME7Jh0HcIH72c26aMAgUA; __gpi=UID=00001106c99d276d:T=1754163992:RT=1754166203:S=ALNI_MZrXyx8Ww-Gj-HQkMsEep8YutPaig; __eoi=ID=99c6d9000ca1b8b8:T=1754163992:RT=1754166203:S=AA-AfjYYyn9nry1Lo0brlspxZ9d9; _gat_gtag_UA_29446588_1=1; FCNEC=%5B%5B%22AKsRol-XjIiTS7Q4wt_NgCY4TyEhPnomP5k7N9Q_XN-bCM9LjLBhQ9w-lzUqlxdY4zzACsiZTvZMWajcVQTEuRsrAYv8XGpI1Z-ZYQ2jTq6U2-3CTurk_iYGFiX9whRul-nGFbyyiWfxZfk2fI27pD78Z67o3xYhjg%3D%3D%22%5D%5D',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    return response
# %%

response = request_content("Ada wong")
if response.status_code != 200:
    print("não foi possível realizar a extração")
# %%

soup = BeautifulSoup(response.text)

# %%
def get_basic_infos(soup):
    data = {}
    page = soup.find('div', 'td-page-content')
    paragrafo = page.find_all('p')[1]
    ems = paragrafo.find_all('em')  
    for i in ems:
        chave, valor = i.text.split(':')
        chave = chave.strip(" ")
        data[chave] = valor
    name = soup.find('h1', 'entry-title')
    name = name.find('span')
    personagem = name.text.strip("<span")
    chave, valor = personagem.split("|")
    dicio = dict(personagem=valor)
    juncao = {**dicio ,**data}
    return juncao
    

# %%

infos = get_basic_infos(soup)

infos

# %%

alex = request_content("Alex Wesker")
soup_alex = BeautifulSoup(alex.text)
info_alex = get_basic_infos(soup_alex)
info_alex

# %%

leon = request_content("leon s. kennedy")
soup_leon = BeautifulSoup(leon.text)
info_leon = get_basic_infos(soup_leon)
info_leon