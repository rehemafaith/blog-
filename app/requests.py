import requests




def get_quotes():
    url='http://quotes.stormconsultancy.co.uk/random.json'
    pos= requests.get(url)
    quotes = pos.json()
    return quotes