import requests


def lin(txt):
    print('~~' * 22)
    print(txt.center(40))
    print('~~' * 22)


API_KEY = 'abcc1547de3101eccf9656fc6520bd1d'
cidade = "Mongaguá"
lat = -24.0924
lon = -46.6213
link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=pt_br'

# pegando informaçoes sobre minha cidade

requisição = requests.get(link) # pega informações do link
requisição_dic = requisição.json() # transforma as informações do link em um dicionário

descrição = requisição_dic['weather'][0]['description']
temperatura = requisição_dic['main']['temp'] - 273.15
vento = requisição_dic['wind']['speed']


lin('PREVIÇÃO DO TEMPO')
print(f'''MONGAGUÁ:
Descição: {descrição}
Temperatura: {temperatura:.0f}
Ventos: {vento}''')