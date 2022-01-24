import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.bna.com.ar/Personas"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
soup = soup.find_all('table', class_='table cotizacion')[0]
headers = [header.text for header in soup.find_all('th')]
results = [[cell.getText() for i, cell in enumerate(row.find_all('td'))]
           for row in soup.find_all('tr')]
results.pop(0)
first_row = ['Dia', headers[0], '']
second_row = ['Moneda', headers[1], headers[2]]
dolar = results[0]
euro = results[1]
real = results[2]
table_monedas = [first_row, second_row, dolar, euro, real]
df = pd.DataFrame(table_monedas)
df.to_excel('monedas.xlsx', index=False)
