import requests
import json
from config import token_apilayer

#ошибки
class APIException (Exception):
    pass

headers= {
          "apikey": token_apilayer
        }
spisok={}

helping = 'список доступных комманд:\n/help - помощь\n/values - список конвертируемых валют\n/conv - команда на конвертацию например: /conv 5 USD RUB (конвертирует пять долларов в рубли)'
class ConverterValyut :
    @staticmethod
    # список конвертируемых валют
    def list_valyuta():
        url = "https://api.apilayer.com/currency_data/list"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        # result = response.text
        result = json.loads(response.content)
        global spisok
        spisok = result['currencies']
        vivod = 'доступные валюты'
        for i in result['currencies']:
            vivod = '\n'.join((vivod, (i + ':' + str(result['currencies'][i]))))
        #print(spisok['rub'.upper()])
        return vivod

    @staticmethod
    #конвертация
    def get_price(base, quote, amount):
        #print (base, quote, amount)
        ConverterValyut.list_valyuta()
        #print(type(amount))
        try:
            if base.upper() not in spisok.keys() or quote.upper() not in spisok.keys():
                raise APIException ('проверьте правильность написания введенных наименований валют')
            if not amount.isdigit():
                raise APIException('количество валют не является числом')
        except APIException as e:
            return e
        url = f"https://api.apilayer.com/currency_data/convert?to={quote}&from={base}&amount={amount}"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        # result = response.text
        # print(result)
        result = json.loads(response.content)
        vivod = f"Согласно курсу валют\n {amount} {base} = {round(result['result'], 2)} {quote}"
        # for i in result['info']:
        #  vivod = '\n'.join((vivod, (i + ':' + str(result['currencies'][i]))))
        #print(vivod)
        return vivod

