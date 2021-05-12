from slack_sdk.webhook import WebhookClient
import json
import time
import os
from selenium import webdriver


def lambda_handler(event, context):
    build_webdriver()
    response_message = hit_webhook()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello Rodney'+response_message+' Lambda!')
    }

def hit_webhook():
    url = 'https://webhook.site/8bea820e-bbdd-4486-b606-fb1963e066d2'
    messages = [{'message': 'Rodney'}]

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    webhook = WebhookClient(url)
    print('This is my fucking Function')

    response = webhook.send(text=json.dumps(messages))
    print(response)
    return url
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def build_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--enable-logging')
    options.add_argument('--log-level=0')
    options.add_argument('--v=99')
    options.add_argument('--single-process')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    options.binary_location = os.getcwd() + "/bin/headless-chromium" 
    driver = webdriver.Chrome('./chromedriver', options=options)
    enable_download_headless(driver, "/tmp")
    url = 'https://dweet.io/follow/thecore'
    driver.get(url)
    time.sleep(3)
    print(driver.find_element_by_xpath('//a[@href="#raw"]').text)

