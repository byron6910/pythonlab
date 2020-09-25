import requests
from bs4 import BeautifulSoup
import urllib

def run():
    for i in range(1,5):
        response=requests.get('https://xkcd.com/{}'.format(i))
        soup=BeautifulSoup(response.content,'html.parser')
        image_container=soup.find(id='comic')
        image_url=image_container.find('img')['src']
        image_name=image_url.split('/')[-1] #acceder desde la ultima.
        print('descargando la imagen {}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url),image_name)


if __name__=='__main__':
    run()