import requests
from sys import argv, exit

# get response
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    exit()

# get price of bitcoin
res = response.json()
price = res['bpi']['USD']['rate'].replace(',','')
price = float(price)

# check and get argument
if len(argv) != 2:
    exit('Missing command-line argument')
else:
    try:
        number = float(argv[1])
    except:
        exit('Command-line argument is not a number')

# calculate price
total = number * price

print(f'${total:,.4f}')