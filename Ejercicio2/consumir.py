# Special IMPORTS
import time
import json
import psycopg2

from json import dumps
from config import config
from slack_sdk.webhook import WebhookClient

from selenium import webdriver


def test_request2(p_time):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
    url = 'https://dweet.io/follow/thecore'
    driver.get(url)
    time.sleep(3)
    for i in range(p_time):
        driver.refresh()
        time.sleep(3)
        driver.find_element_by_xpath('//a[@href="#raw"]').click()
        raw_element = driver.find_element_by_id('thing-data-raw')
        y = json.loads(raw_element.text)
        test_save('temperature', y['temperature'])
        test_save('humidity', y['humidity'])
        time.sleep(55)

## Guardar BD
def test_save(type_weather, value_number):
    conexion = None
    try:
        # Lectura de los parámetros de conexion
        params = config()

        # Conexion al servidor de PostgreSQL
        conexion = psycopg2.connect(**params)

        # Creación del cursor
        cur = conexion.cursor()

        # Ejecución de una consulta con la version de PostgreSQL
        cur.execute("INSERT INTO weather (type_weather, value_number) VALUES (%s, %s)", (type_weather, value_number))

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
        cur.execute("Select * from weather order by date_at")

        records = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
    return records


def hit_webhook():
    # Catch Data of BD
    records = test_get_data()

    # Service webhook
    url = 'https://webhook.site/8bea820e-bbdd-4486-b606-fb1963e066d2'
    messages = []
    for row in records:
        messages.append({
            'type_weather': row[1],
            'date': str(row[2]),
            'value_number': str(row[3])
        })

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    webhook = WebhookClient(url)

    response = webhook.send(text=dumps(messages))
    print(response)


if __name__ == '__main__':
    p_time = 15  # time
    test_request2(p_time)
    hit_webhook()
