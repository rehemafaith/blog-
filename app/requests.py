import urllib.request,json
from .models import Quotes

# Getting api key
# api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global base_url
    # api_key = app.config['NEWS_API_KEY']
    base_url = app.config['QUOTES_API_BASE_URL']
    

def get_quotes():
    '''
    Function that gets the json to our url request
    '''

    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None 

        if get_quotes_response['quotes']:
            quotes_results_list = get_quotes_response['quotes']
            quotes_results = process_results(quotes_results_list)

    return quotes_results

def process_results(quotes_list):
    '''
    Function that processes the quotes result and transform them to a list 
    of objects
    Args:
        quotes_list: A list of dictionaries that contain news sources 
    Returns :
          quotes_results: A list of news objects 
    '''
    
    quotes_results = []
    for quotes_item in quotes_list:
        id = quotes_item.get('id')
        author = quotes_item.get('author')
        quote = quotes_item.get ('quote')
        

    
        quotes_object = Quotes(id,author,quote)
        quotes_results.append(quotes_object)

    return quotes_results

