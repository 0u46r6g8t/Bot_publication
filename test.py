for result in results:
    print(result)
#bot = Bot()
#json_news = {
#    'news': 'O mundo é ainda melhor com jogos de videos game',
#    'link': 'www.facebook.com'
#}
#bot.publication(json_news, "feed")
#bot.success_connection_mysql()
from bs4 import BeautifulSoup
import requests

url = 'https://www.tecmundo.com.br/voxel/jogos/cyberpunk-2077'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

req = requests.get(url,headers= header)

html = req.text

soup = BeautifulSoup(html,'html.parser')

colecao = soup.find_all(class_='z--w-1-2 z--col z--pt-16 z--pb-16') 

articles = soup.find_all(class_="tec--card tec--card--top")
artist_name_list_items = articles.find_all('a')
print(artist_name_list_items)
#for item in colecao:
#    soup = BeautifulSoup(item)

#    items = soup.find('a')
 #   print(item.text)