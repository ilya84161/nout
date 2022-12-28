import requests, json   #конвертация
from config import token_apilayer

headers= {
          "apikey": token_apilayer
        }

def get_price(base, quote, amount):
  url = f"https://api.apilayer.com/currency_data/convert?to={quote}&from={base}&amount={amount}"
  payload = {}
  response = requests.request("GET", url, headers=headers, data=payload)
  status_code = response.status_code
  #result = response.text
  #print(result)

  result = json.loads(response.content)
  vivod = f"Согласно курсу валют {amount}{base}={round(result['result'], 2)}{quote}"
  #for i in result['info']:
  #  vivod = '\n'.join((vivod, (i + ':' + str(result['currencies'][i]))))
  print(vivod)
  #return vivod

get_price('usd', 'rub', '10')