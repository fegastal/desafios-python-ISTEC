from requests_html import HTMLSession

s = HTMLSession()

query = 'lisbon'
url = f'https://www.google.com/search?q=wheater+{query}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})

temp = r.html.find('span#wob_tm', first=True).text

if temp in range(0, 10):
    print(f"Temperatura de {temp} graus em Lisboa. Utilização de um casaco quente!".format(temp))
elif temp in range(11, 20):
    print(f"Temperatura de {temp} graus em Lisboa. Utilização de um casaco leve!".format(temp))
else:
    print(f"Temperatura de {temp} graus em Lisboa. Não é preciso levar casaco!".format(temp))
