from consumir import test_get_data, test_request
from json import dumps
from slack_sdk.webhook import WebhookClient
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    
    # coins to search
    coins = ['EUR', 'CLP', 'PEN']
    # Request Yahoo! and Save
    test_request(coins)

    # Catch Data of BD
    records = test_get_data()

    # Service webhook
    url = 'https://webhook.site/8bea820e-bbdd-4486-b606-fb1963e066d2'
    messages =  []
    for row in records:
        messages.append({
            'CoinDollar': row[3],
            'date': str(row[2]),
            'Change_value': str(row[1])
        })

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    webhook = WebhookClient(url)

    response = webhook.send(text=dumps(messages))

    print(response)
    return dumps(messages)

app.run()