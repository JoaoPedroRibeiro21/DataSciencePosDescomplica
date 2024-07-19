#Ler arquivos da internet

import requests

ler = requests.get("https://wiki.sj.ifsc.edu.br/images/4/4a/Ecoshower.txt")

with open("arquivo001.txt", "wb") as arquivo:
    arquivo.write(ler.content)