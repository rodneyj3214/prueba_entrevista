from typing import ChainMap
from datetime import datetime
from requests.models import parse_url
from config import config

# Special IMPORTS
import bs4
import psycopg2
import requests


## PUNTO 1 Consultar URL DE YAHOO
def test_request(coins):
    # record of coins
    for i in coins:
        print('*****CONSULTANDO  Yahoo Page y guardando BD*****')
        url = 'https://finance.yahoo.com/quote/'+i+'USD%3DX/history?p='+i+'USD%3DX'# URL for coin

        response = requests.get(url)
        print('*********'+i+'************')
        if response.status_code == 200:
            print('success Yahoo Page\n')
            # soup of request Test
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            
            # filter 5 tables start rows(Days)
            for day in soup.table.tbody.find_all('tr', limit = 5):
                # Find te Change value (Adjust Value for day)
                chage_value = day.find_all('td')[5].span.get_text()

                # Find the first Colum for DATE
                str_date  = day.find_all('td')[0].span.get_text()
                # Fromat date for 
                date = datetime.strptime(str_date, '%b %d, %Y')
                
                ## GUARDAR REGISTROS
                test_save(date, chage_value, i)

## Guardar BD
def test_save(date, change_value, coin):
    conexion = None
    try:
        # Lectura de los parámetros de conexion
        params = config()

        # Conexion al servidor de PostgreSQL
        conexion = psycopg2.connect(**params)

        # Creación del cursor
        cur = conexion.cursor()

        # Ejecución de una consulta con la version de PostgreSQL
        cur.execute("INSERT INTO test (change_value, date_coin, name_coin) VALUES (%s, %s, %s)", (change_value, date, coin))

        # Cierre de la comunicación con PostgreSQL
        conexion.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
# Catch the bd info

def test_get_data():
    conexion = None
    records = None
    try:
        # Read Config
        params = config()

        # Connect wirh params
        conexion = psycopg2.connect(**params)

        # Cur creation
        cur = conexion.cursor()

        # Select of information
        cur.execute("Select * from test order by name_coin")

        records = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
    return records

if __name__ == '__main__':
    # coins to search
    coins = ['EUR', 'CLP', 'PEN']
    test_request(coins)
