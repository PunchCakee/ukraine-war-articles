import requests
import json
def main():
    url = ('https://newsapi.org/v2/everything?'
           'q=Ukraine conflict&'
           'sources=cnn&'
           'sortBy=new&'
           'apiKey=') #place your api key here
    response = requests.get(url)
    
    with open('news.json','w+') as file:
        json.dump(response.json(), file)

if __name__ == '__main__':
    main()
