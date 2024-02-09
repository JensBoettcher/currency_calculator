import requests

API_KEY = 'fca_live_RP1amP2FH2I69FXYUp0rmfetEGk0RuMBcGDMWygo'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = [ "EUR", "CHF", "CAD", "USD"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break

    # convert the currencies in my currency (Euro)
    data = convert_currency(base)
    if not data:
        continue

    del data [base] # this will delete Euro in the output
    for ticker, value in data.items():
        print(f"{ticker}: {value}")