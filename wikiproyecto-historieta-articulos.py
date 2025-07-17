import requests
import re
from bs4 import BeautifulSoup
from time import sleep


ESWIKI = "https://es.wikipedia.org"
PAGINA_INICIAL = "/wiki/Categor%C3%ADa:Wikiproyecto:Historieta/Art%C3%ADculos"

wiki_url = f"{ESWIKI}{PAGINA_INICIAL}"
paginas = []
n_pag = 1
hay_siguiente = True

while hay_siguiente:
    sleep(0.25)
    wiki_r = requests.get(wiki_url)
    wiki_soup = BeautifulSoup(wiki_r.text, "html.parser")
    paginas.append(wiki_soup)
    pag_siguiente = wiki_soup.find("a", string=re.compile("siguiente"))
    if pag_siguiente:
        print(f"Página {n_pag}")
        n_pag += 1
        href_pag_siguiente = pag_siguiente.get("href")
        wiki_url = f"{ESWIKI}{href_pag_siguiente}"
    else:
        print("No hay más páginas.")
        hay_siguiente = False
