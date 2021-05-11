
from config import config
from consumir import test
from json import dumps
from httplib2 import Http
import psycopg2
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True

def get_data():
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
        cur.execute("Select * from test")

        records = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexión finalizada.')
    return records

@app.route('/', methods=['GET'])
def home():
    
    records = get_data()
    print("Print each row and it's columns values")
    for row in records:
        print('Rodney*****************************+')
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")
    
    url = 'https://webhook.site/8bea820e-bbdd-4486-b606-fb1963e066d2'
    bot_message = {
        'text' : 'Hello from a Python script!'}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)
    return "Hola"

app.run()